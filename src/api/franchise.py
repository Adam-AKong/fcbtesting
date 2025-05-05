from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from api.models import Franchise

router = APIRouter(prefix="/franchise", tags=["Franchise"])


@router.get("/get/{franchise_id}", response_model=Franchise)
def get_franchise(franchise_id: int):
    """
    Get franchise by ID.
    """
    # Placeholder for actual database call
    franchise = Franchise(
        id=franchise_id,
        name="Franchise Name",
        description="Franchise Description",
    )
    return franchise

@router.post("{user_id}/review/{franchise_id}", status_code=status.HTTP_204_NO_CONTENT)
def make_franchise_review(user_id: int, franchise_id: int, comment: str):
    """
    Make a review for a franchise.
    """
    # Placeholder for actual database call
    if not comment:
        raise HTTPException(status_code=400, detail="Comment cannot be empty")
    # Save the review to the database