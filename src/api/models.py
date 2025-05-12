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
    id: int
    user_id: int    
    char1_id: int
    char2_id: int
    vote1: int
    vote2: int
    winner_id: int
    
    
class User(BaseModel):
    id: int
    name: str