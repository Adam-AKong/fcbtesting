from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/battle", tags=["Battle"])