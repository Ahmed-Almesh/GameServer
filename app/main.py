from xml.etree.ElementInclude import include

from fastapi import FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import TicTacToe, users, GameLobbyRouter

app = FastAPI(
    title="Local games",
    description= "A game website",
    version= "1.0.0"
)

app.include_router(TicTacToe.TicTacToe_router)
app.include_router(users.user_router)
app.include_router(GameLobbyRouter.game_lobby_router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}