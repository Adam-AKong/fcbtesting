from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import sqlalchemy
from src import database as db
from datetime import datetime

from src.api.models import User

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/get/{user_id}", response_model=User)
def get_user(user_id: int):
    """
    Get User by ID.
    """
    # Placeholder for actual database call
    user = User(
        id=user_id,
        name="User Name",
    )

@router.post("/make", status_code=status.HTTP_204_NO_CONTENT)
def make_user(name: str):
    """
    Make a new user.
    """
    # Placeholder for actual database call
    if not name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    # Save the user to the database
    with db.engine.begin() as connection:
        connection.execute(
            sqlalchemy.text("""
                INSERT INTO "user" (name)
                VALUES (:name)
            """),
            {
             "name": name,
             },
        )
    
    