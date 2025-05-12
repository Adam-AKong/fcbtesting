from datetime import timedelta, datetime

import sqlalchemy
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import DateTime

from src.api.models import Battle, BattleResult, Character
from src import database as db

router = APIRouter(prefix="/battle", tags=["Battle"])



def calculate_winner(connection, battle: Battle) -> int:
    """
    Calculate the winner of a battle based on the votes and character stats.
    """
    character1 = connection.execute(
        sqlalchemy.text(
            """
            SELECT *
            FROM character
            WHERE id = :id
            """
        ),
        [{"id": battle.char1_id}]
    ).one()
    character2 = connection.execute(
        sqlalchemy.text(
            """
            SELECT *
            FROM character
            WHERE id = :id
            """
        ),
        [{"id": battle.char2_id}]
    ).one()
    # Calculate the winner based on the votes and character stats
    character1_score = (character2.health / (character1.strength * character1.speed)) * (0.9 ^ battle.vote1)
    character2_score = (character1.health / (character2.strength * character2.speed)) * (0.9 ^ battle.vote2)
    if character1_score < character2_score:
        return battle.char1_id
    else:
        return battle.char2_id

@router.get("/get/{battle_id}", response_model=BattleResult)
def get_battle_result(battle_id: int):
    """
    Get the result of a battle by its ID.
    """
    with db.engine.begin() as connection:
        battle = connection.execute(
            sqlalchemy.text(
                """
                SELECT *
                FROM battle
                WHERE id = :id
                """
            ),
            [{"id": battle_id}]
        ).one()
        
        
        if battle.end > datetime.now():
            return BattleResult(
                battle_id=battle.id,
                char1_id=battle.char1_id,
                char2_id=battle.char2_id,
                vote1=battle.vote1,
                vote2=battle.vote2,
                winner_id=None,
                start=battle.start_date,
                end=battle.end_date,
                finished=False
            )
        
        if battle.winner_id is None:
            # Calculate the winner if not already set
            winner = calculate_winner(connection, battle)
            connection.execute(
                sqlalchemy.text(
                    """
                    UPDATE battle
                    SET winner_id = :winner
                    WHERE id = :id
                    """
                ),
                [{"winner": winner, "id": battle.id}]
            )
    
        return BattleResult(
            battle_id=battle.id,
            char1_id=battle.char1_id,
            char2_id=battle.char2_id,
            vote1=battle.vote1,
            vote2=battle.vote2,
            winner_id=battle.winner_id,
            start=battle.start_date,
            end=battle.end_date,
            finished=True
        )

@router.get("/get/{character_id}", response_model=list[Battle])
def character_participation(character_id: int):
    """
    Get a list of battles a character has fought in.
    """
    battles = []
    with db.engine.begin() as connection:
        participation = connection.execute(
            sqlalchemy.text(
                """
                SELECT *
                FROM battle
                WHERE char1_id = :char OR char2_id = :char
                """
            ),
            [{"char": character_id}]
        ).fetchall()
        for r in participation:
            battles.append(
                Battle(
                    id = r.id,
                    user_id = r.user_id,
                    char1_id = r.char1_id,
                    char2_id = r.char2_id,
                    vote1 = r.vote1,
                    vote2 = r.vote2,
                    winner_id = r.winner_id
                )
            )
    return battles

@router.get("/get/{user_id}", response_model=list[Battle])
def user_participation(user_id: int):
    """
    Get a list of battles a user has participated in.
    """
    # Proper
    battles = []
    with db.engine.begin() as connection:
        participation = connection.execute(
            sqlalchemy.text(
                """
                SELECT count(battle_id)
                FROM votes
                WHERE user_id = :user
                GROUP BY user_id
                """
            ),
            [{"user": user_id}]
        ).fetchall()
        for r in participation:
            battles.append(
                Battle(
                    id = r.id,
                    user_id = r.user_id,
                    char1_id = r.char1_id,
                    char2_id = r.char2_id,
                    vote1 = r.vote1,
                    vote2 = r.vote2,
                    winner_id = r.winner_id
                )
            )
    return battles

@router.post("/vote/{user_id}/{battle_id}/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
def battle_vote(user_id: int, battle_id: int, character_id: int):
    """
    Vote for a character during an active battle.
    """
    vote1_i = 0
    vote2_i = 0
    
    with db.engine.begin() as connection:
        battle_info = connection.execute( # Check for unique battle and character existence
            sqlalchemy.text(
                """
                SELECT *
                FROM battle
                WHERE battle_id = :battle
                    AND (char1_id = :char OR char2_id = :char)
                RETURNING char1_id, char2_id
                """
            ),
            [{"battle": battle_id,
              "char": character_id}]
        ).one()

        user_check = connection.execute(
            sqlalchemy.text(
                """
                SELECT *
                FROM battle_votes
                WHERE battle_id = :battle
                    AND user_id = :user
                """
            ),
            [{"battle": battle_id,
              "user": user_id}]
        )
        if user_check:
            raise Exception("Found a vote matching this user ID.")
        
        match character_id:
            case(battle_info.char1_id):
                vote1_i += 1
            case(battle_info.char2_id):
                vote2_i += 1
        
        connection.execute(
            sqlalchemy.text( # This can work, but we can also calculate this by pulling the sum(votes) from battle_votes
                """
                UPDATE battle
                SET vote1 += vote1_d, vote2 += vote2_d
                WHERE battle_id = :battle
                """
            ),
            [{"battle": battle_id}]
        )
        connection.execute(
            sqlalchemy.text(
                """
                INSERT INTO battle_votes (battle_id, user_id)
                VALUES (:battle, :user);
                """
            ),
            [{"battle": battle_id,
              "user": user_id}]
        )
    pass

@router.post("/make", response_model=BattleResult)
def create_battle(Battle: Battle):
    """
    Create a battle between two characters and return its id.
    """
    # Assuming duration is in hours
    
    print("[DEBUG] Creating battle")
    
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=Battle.duration)
    
    with db.engine.begin() as connection:
        print("[DEBUG] Inserting battle into database")
        battle_id = connection.execute(
            sqlalchemy.text(
                """
                INSERT INTO battle (user_id, char1_id, char2_id, start_date, end_date)
                VALUES (:user, :char1, :char2, :start, :end)
                RETURNING id
                """
            ),
            [{"user": Battle.user_id,
              "char1": Battle.char1_id,
              "char2": Battle.char2_id,
              "start": start_time,
              "end": end_time
              }]
        ).scalar_one()
        
    return BattleResult(
        battle_id = int(battle_id),
        char1_id = Battle.char1_id,
        char2_id = Battle.char2_id,
        vote1 = 0,
        vote2 = 0,
        winner_id = None,
        start = start_time,
        end = end_time,
        finished = False
    )