from datetime import timedelta, datetime

import sqlalchemy
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import DateTime

from src.api.models import Battle, Character
from src import database as db

router = APIRouter(prefix="/battle", tags=["Battle"])

@router.get("/get/{battle_id}", response_model=Battle)
def get_battle_result(battle_id: int):
    """
    Get the result of a battle by its ID.
    """
    with db.engine.begin as connection:
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
    
        return Battle(
            id=battle.id,
            user_id=battle.user_id,
            char1_id=battle.char1_id,
            char2_id=battle.char2_id,
            vote1=battle.vote1,
            vote2=battle.vote2,
            winner_id=battle.winner_id,
        )

@router.get("/get/{character_id}", response_model=list[Battle])
def character_participation(character_id: int):
    """
    Get a list of battles a character has fought in.
    """
    battles = []
    with db.engine.begin as connection:
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
    with db.engine.begin as connection:
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
    
    with db.engine.begin as connection:
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

@router.post("/make", status_code=status.HTTP_204_NO_CONTENT)
def create_battle(user_id: int, character_1: int, character_2: int, start_date: datetime, duration: int):
    """
    Create a battle between two characters.
    """
    # Assuming duration is in hours
    with db.engine.begin as connection:
        connection.execute(
            sqlalchemy.text(
                """
                INSERT INTO battle (user_id, char1_id, char2_id, start, end)
                VALUES (:user, :char1, :char2, :start, :end);
                """
            ),
            [{"user": user_id,
              "char1": character_1,
              "char2": character_2,
              "start": start_date,
              "end": start_date + timedelta(hours=duration)}]
        )
    pass