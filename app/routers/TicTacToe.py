from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

TicTacToe_router = APIRouter(
    prefix="/TicTacToe",
    tags=["TicTacToe"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


