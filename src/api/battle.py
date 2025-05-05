from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.api.models import Battle, Character

router = APIRouter(prefix="/battle", tags=["Battle"])

@router.get("/get/{battle_id}", response_model=Battle)
def get_battle_result(battle_id: int):
    """
    Get the result of a battle by its ID.
    """
    pass

@router.get("/get/{character_id}", response_model=list[Battle])
def character_participation(character_id: int):
    """
    Get a list of battles a character has fought in.
    """
    pass

@router.get("/get/{user_id}", response_model="")
def user_participation(user_id: int):
    """
    Get a list of battles a user has participated in.
    """
    pass

@router.get("/vote/{battle_id}/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
def battle_vote(battle_id: int, character_id: int):
    """
    Vote for a character during an active battle.
    """
    pass

@router.get("/make", status_code=status.HTTP_204_NO_CONTENT)
def create_battle(character_1: int, character_2: int, duration: int):
    """
    Create a battle between two characters.
    """
    pass