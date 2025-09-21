from fastapi import FastAPI, APIRouter
from sqlalchemy.orm import defer

user_router = APIRouter()

@user_router.get("/users/", tags= ["users"])
async def read_users():
    return  [{"username": "Rick"}, {"username":"Morty"}]

@user_router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}