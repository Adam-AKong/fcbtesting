from fastapi import FastAPI
from src.api import character, franchise, battle, user


app = FastAPI()

app.include_router(character.router)
app.include_router(franchise.router)
app.include_router(battle.router)
app.include_router(user.router)