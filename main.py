from fastapi import FastAPI
from src.api import character, franchise, battle


app = FastAPI()

app.include_router(character.router)
app.include_router(franchise.router)
app.include_router(battle.router)