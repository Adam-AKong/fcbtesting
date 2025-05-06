from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import sqlalchemy
from src import database as db

from src.api.models import Character, C_Review


router = APIRouter(prefix="/character", tags=["Character"])


@router.get("/get/{character_id}", response_model=Character)
def get_character(character_id: int):
    """
    Get character by ID.
    """
    
    with db.engine.begin() as connection:
        character = connection.execute(
            sqlalchemy.text("""
                SELECT id, name, description, rating, strength, speed, health
                FROM character
                WHERE id = :id
            """),
            {
                "id": character_id
            }
        ).scalar_one()
    
    character = Character(
        name=character.name,
        description=character.description,
        rating=character.rating,
        strength=character.strength,
        speed=character.speed,
        health=character.health,
    )
    return character




@router.get("/list/{user_id}", response_model=list[Character])
def get_user_characters(user_id: int):
    """
    Get all characters made by user.
    """

    with db.engine.begin() as connection:
        characters = connection.execute(
            sqlalchemy.text("""
                SELECT id, name, description, rating, strength, speed, health
                FROM character
                WHERE user_id = :user_id
            """),
            {
                "user_id": user_id
            }
        ).all()
    
    characters = [
        Character(
            id=character.id,
            name=character.name,
            description=character.description,
            rating=character.rating,
            strength=character.strength,
            speed=character.speed,
            health=character.health,
        )
        for character in characters
    ]
    return characters

class Returned_Review(BaseModel):
    user_id: int
    comment: str

@router.get("/get_review/{character_id}", response_model=list[Returned_Review])
def get_character_review(character_id: int):
    """
    Get all reviews for a given character referencing its id.
    """
    with db.engine.begin() as connection:
        comments = connection.execute(
            sqlalchemy.text("""
                SELECT user_id, comment
                FROM c_review
                WHERE char_id = :char_id
            """),
            {
                "char_id": character_id
            }
        ).all()

    all_comments = []
    for comment in comments:
        all_comments.append(
            Returned_Review(
                user_id = comment.user_id,
                comment = comment.comment
            )
        )

    return all_comments


@router.get("/leaderboard", response_model=list[Character])
def get_leaderboard():
    """
    Get the leaderboard of characters.
    """
    
    with db.engine.begin() as connection:
        characters = connection.execute(
            sqlalchemy.text("""
                SELECT id, name, description, rating, strength, speed, health
                FROM character
                ORDER BY rating DESC
                LIMIT 10
            """)
        ).all()
    
    characters = [ 
        Character(
            id=character.id,
            name=character.name,
            description=character.description,
            rating=character.rating,
            strength=character.strength,
            speed=character.speed,
            health=character.health,
        )
        for character in characters
    ]
    
    return characters

class Returned_Character(BaseModel):
    char_id: int
    user_id: int
    name: str
    description: str
    rating: float
    strength: float
    speed: float
    health: float

@router.post("/make", response_model=Returned_Character)
def make_character(user_id: int, character: Character):
    """
    Create a new character.
    """
    # Placeholder for actual database call
    
    with db.engine.begin() as connection:
        char_id = connection.execute(
            sqlalchemy.text("""
                INSERT INTO character (user_id, name, description, rating, strength, speed, health)
                VALUES (:user_id, :name, :description, :rating, :strength, :speed, :health)
                RETURNING id
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
        ).scalar_one()

    new_character = Returned_Character(
        char_id = char_id,
        user_id = user_id,
        name = character.name,
        description = character.description,
        rating = character.rating,
        strength = character.strength,
        speed = character.speed,
        health = character.health
    )

    return new_character


@router.post("/review/{char_id}", status_code=status.HTTP_204_NO_CONTENT)
def review_character(user_id: int, character_id: int, comment: str):
    """
    Review a character.
    """
    if not comment:
        raise HTTPException(status_code=400, detail="Comment cannot be empty")

    with db.engine.begin() as connection:
        connection.execute(
            sqlalchemy.text("""
                INSERT INTO c_review (user_id, char_id, comment)
                VALUES (:user_id, :char_id, :comment)
            """),
            {
                "user_id": user_id,
                "char_id": character_id,
                "comment": comment
            },
        )
