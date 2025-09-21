from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header


game_lobby_router = APIRouter(
    prefix="/GameLobby",
    tags=["GameLobby"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@game_lobby_router.get("/{game_id}")
async def get_game(game_id: int):
    raise NotImplemented
