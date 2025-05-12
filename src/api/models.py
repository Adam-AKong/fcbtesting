from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Character(BaseModel):
    name: str
    description: str
    rating: float
    strength: float
    speed: float
    health: float
    
class Franchise(BaseModel):
    name: str
    description: str
    
class C_Review(BaseModel):
    user_id: int
    char_id: int
    comment: str
    
class F_Review(BaseModel):
    user_id: int
    franchise_id: int
    comment: str
    
class Battle(BaseModel):
    user_id: int    
    char1_id: int
    char2_id: int
    duration: int
    
class BattleResult(BaseModel):
    battle_id: int
    char1_id: int
    char2_id: int
    vote1: int
    vote2: int
    winner_id: Optional[int]
    start: datetime
    end: datetime
    finished: bool
    
    
class User(BaseModel):
    id: int
    name: str