from fastapi import FastAPI
from api import character, franchise
from src.api import battle

app = FastAPI()

app.include_router(character.router)
app.include_router(franchise.router)
app.include_router(battle.router)