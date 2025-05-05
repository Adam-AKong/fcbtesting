import sqlalchemy
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.api.models import Battle, Character
# from src import database as db

router = APIRouter(prefix="/battle", tags=["Battle"])

@router.get("/get/{battle_id}", response_model=Battle)
def get_battle_result(battle_id: int):
    """
    Get the result of a battle by its ID.
    """
    # More proper code
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
        connection.execute(
            sqlalchemy.text(
                
            )
        )
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
    pass

@router.post("/make", status_code=status.HTTP_204_NO_CONTENT)
def create_battle(character_1: int, character_2: int, duration: int):
    """
    Create a battle between two characters.
    """
    pass