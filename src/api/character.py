from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import sqlalchemy
from src import database as db

from src.api.models import Character


router = APIRouter(prefix="/character", tags=["Character"])


@router.get("/get/{character_id}", response_model=Character)
def get_character(character_id: int):
    """
    Get character by ID.
    """
    # Placeholder for actual database call
    character = Character(
        id=character_id,
        name="Character Name",
        description="Character Description",
        rating=0,
        strength=0,
        speed=0,
        health=0,
    )
    return character




@router.get("/list/{user_id}", response_model=list[Character])
def get_user_characters(user_id: int):
    """
    Get all characters made by user.
    """
    # Placeholder for actual database call
    characters = [
        Character(
            id=1,
            name="Character 1",
            description="Description 1",
            rating=0,
            strength=0,
            speed=0,
            health=0,
        ),
        Character(
            id=2,
            name="Character 2",
            description="Description 2",
            rating=0,
            strength=0,
            speed=0,
            health=0,
        ),
    ]
    return characters

@router.get("/leaderboard", response_model=list[Character])
def get_leaderboard():
    """
    Get the leaderboard of characters.
    """
    # Placeholder for actual database call
    characters = [
        Character(
            id=1,
            name="Character 1",
            description="Description 1",
            rating=5.0,
            strength=10.0,
            speed=8.0,
            health=100.0,
        ),
        Character(
            id=2,
            name="Character 2",
            description="Description 2",
            rating=4.5,
            strength=9.0,
            speed=7.0,
            health=90.0,
        ),
    ]
    return characters


@router.post("/make", status_code=status.HTTP_204_NO_CONTENT)
def make_character(user_id: int, character: Character):
    """
    Create a new character.
    """
    # Placeholder for actual database call
    
    with db.engine.begin() as connection:
        connection.execute(
            sqlalchemy.text("""
                INSERT INTO characters (user_id, name, description, rating, strength, speed, health)
                VALUES (:user_id, :name, :description, :rating, :strength, :speed, :health)
            """),
            {
                "user_id": user_id,
                "name": character.name,
                "description": character.description,
                "rating": character.rating,
                "strength": character.strength,
                "speed": character.speed,
                "health": character.health,
            },
        )


@router.post("/review/{char_id}", status_code=status.HTTP_204_NO_CONTENT)
def review_character(user_id: int, character_id: int, comment: str):
    """
    Review a character.
    """
    # Placeholder for actual database call
    if not comment:
        raise HTTPException(status_code=400, detail="Comment cannot be empty")
    # Save the review to the database

