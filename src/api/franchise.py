from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import sqlalchemy
from src import database as db

from src.api.models import Franchise

router = APIRouter(prefix="/franchise", tags=["Franchise"])


@router.get("/get/{franchise_id}", response_model=Franchise)
def get_franchise(franchise_id: int):
    """
    Get franchise by ID.
    """
    
    with db.engine.begin() as connection:
        franchise = connection.execute(
            sqlalchemy.text("""
                SELECT NAME, DESCRIPTION
                FROM franchise
                WHERE id = :id
            """),
            {
                "id": franchise_id
                }
        ).scalar_one()
        

    franchise = Franchise(
        name=franchise.name,
        description=franchise.description,
    )
    return franchise

@router.post("/make", status_code=status.HTTP_204_NO_CONTENT)
def make_franchise(franchise: Franchise):
    """
    Create a new franchise.
    """
    
    with db.engine.begin() as connection:
        connection.execute(
            sqlalchemy.text("""
                INSERT INTO franchise (name, description)
                VALUES (:name, :description)
            """),
            {
                "name": franchise.name,
                "description": franchise.description,
            },
        )

@router.post("/review/{franchise_id}", status_code=status.HTTP_204_NO_CONTENT)
def make_franchise_review(user_id: int, franchise_id: int, comment: str):
    """
    Make a review for a franchise.
    """
    # Placeholder for actual database call
    if not comment:
        raise HTTPException(status_code=400, detail="Comment cannot be empty")

    with db.engine.begin() as connection:
        connection.execute(
            sqlalchemy.text("""
                INSERT INTO f_review (user_id, franchise_id, comment)
                VALUES (:user_id, :franchise_id, :comment)
            """),
            {
                "user_id": user_id,
                "franchise_id": franchise_id,
                "comment": comment,
            },
        )