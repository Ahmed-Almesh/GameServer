from contextlib import asynccontextmanager
from xml.etree.ElementInclude import include
from app.database.db_tables import initialize_database
from fastapi import FastAPI

from .dependencies import get_query_token, get_token_header
from .routers import TicTacToe, users, GameLobbyRouter

@asynccontextmanager
async def lifespan(app_server: FastAPI):
    print('start')
    initialize_database()
    yield
    print('end')


app = FastAPI(
    title="Local games",
    description= "A game website",
    version= "1.0.0",
    lifespan=lifespan
)

app.include_router(TicTacToe.TicTacToe_router)
app.include_router(users.user_router)
app.include_router(GameLobbyRouter.game_lobby_router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}