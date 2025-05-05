import sqlalchemy
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.api.models import Battle, Character
from src import database as db

router = APIRouter(prefix="/battle", tags=["Battle"])

@router.get("/get/{battle_id}", response_model=Battle)
def get_battle_result(battle_id: int):
    """
    Get the result of a battle by its ID.
    """
    # Proper
    """
    with db.engine.begin as connection:
        battle = connection.execute(
            sqlalchemy.text(
                
                SELECT *
                FROM battle
                WHERE id = :id
                
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
    """
    # Placeholder
    return Battle(
        id=1,
        user_id=1,
        char1_id=1,
        char2_id=2,
        vote1=0,
        vote2=1,
        winner_id=2
    )

@router.get("/get/{character_id}", response_model=list[Battle])
def character_participation(character_id: int):
    """
    Get a list of battles a character has fought in.
    """
    # Proper
    """
    with db.engine.begin:
        participation = connection.execute(
            sqlalchemy.text(
                SELECT *
                FROM battle
                WHERE char1_id = :char OR char2_id = :char
            ),
            [{"char": character_id}]
        ) # Unsure as to what type this is returning
    return participation
    """
    # Placeholder
    battles = [
        Battle(
            id=1,
            user_id=1,
            char1_id=1,
            char2_id=2,
            vote1=0,
            vote2=1,
            winner_id=2
        ),
        Battle(
            id=2,
            user_id=1,
            char1_id=1,
            char2_id=2,
            vote1=1,
            vote2=0,
            winner_id=1
        )
    ]
    return battles

@router.get("/get/{user_id}", response_model=list[Battle])
def user_participation(user_id: int):
    """
    Get a list of battles a user has participated in.
    """
    # Proper
    """
    with db.engine.begin:
        participation = connection.execute(
            sqlalchemy.text(
                SELECT count(battle_id)
                FROM votes
                WHERE user_id = :user
                GROUP BY user_id
                # Added a comment about this in the Alembic Models py
            ),
            [{"user": user_id}]
        ).scalar_one()
    return participation
    """
    # Placeholder
    battles = [
        Battle(
            id=1,
            user_id=1,
            char1_id=1,
            char2_id=2,
            vote1=0,
            vote2=1,
            winner_id=2
        ),
        Battle(
            id=2,
            user_id=1,
            char1_id=1,
            char2_id=2,
            vote1=1,
            vote2=0,
            winner_id=1
        )
    ]
    return battles

@router.post("/vote/{battle_id}/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
def battle_vote(battle_id: int, character_id: int):
    """
    Vote for a character during an active battle.
    """
    # Proper
    """
    vote1_i = 0
    vote2_i = 0
    
    with db.engine.begin: # Checks both character and battle ids
        battle_info = connection.execute(
            sqlalchemy.text(
                SELECT *
                FROM battle
                WHERE battle_id = :battle
                    AND (char1_id = :char OR char2_id = :char)
                RETURNING char1_id, char2_id
            ),
            [{"battle": battle_id,
              "char": character_id}]
        ).one()
        
        match(character_id): # Treating battle_info as a list right now
            case(battle_info[0]): # 1st
                vote1_d += 1
            case(battle_info[1]): # 2nd
                vote2_d += 1
        
        connection.execute(
            sqlalchemy.text(
                UPDATE battle
                SET vote1 += vote1_d, vote2 += vote2_d
                WHERE battle_id = :battle
            ),
            [{"battle": battle_id}]
        )
    """
    pass

@router.post("/make", status_code=status.HTTP_204_NO_CONTENT)
def create_battle(user_id: int, character_1: int, character_2: int, start_date: int, duration: int):
    """
    Create a battle between two characters.
    """
    # Proper
    """
    with db.engine.begin:
        connection.execute(
            sqlalchemy.text(
                INSERT INTO battle (user_id, char1_id, char2_id, start, end)
                VALUES (:user, :char1, :char2, :start, :end);
            ),
            [{"user": :user_id,
              "char1": character_1,
              "char2": character_2,
              "start": start_date,
              "end": start_date + duration}]
        )
    """
    pass