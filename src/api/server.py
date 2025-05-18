from fastapi import FastAPI
from src.api import battle, character, franchise, user
from starlette.middleware.cors import CORSMiddleware

description = """
Premier Database for all youfictional character needs.
"""
tags_metadata = [
    {"name": "cart", "description": "Place potion orders."},
    {"name": "catalog", "description": "View the available potions."},
    {"name": "bottler", "description": "Bottle potions from the raw magical elixir."},
    {
        "name": "barrels",
        "description": "Buy barrels of raw magical elixir for making potions.",
    },
    {"name": "admin", "description": "Where you reset the game state."},
    {"name": "info", "description": "Get updates on time"},
    {
        "name": "inventory",
        "description": "Get the current inventory of shop and buying capacity.",
    },
]

app = FastAPI(
    title="Fictional Character Brawl",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Adam Kong",
        "email": "aakong@calpoly.edu",
    },
    openapi_tags=tags_metadata,
)

origins = ["https://potion-exchange.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(battle.router)
app.include_router(character.router)
app.include_router(franchise.router)
app.include_router(user.router)


@app.get("/")
async def root():
    return {"message": "Characters are waiting to brawl..."}
