from datetime import timedelta
from http import HTTPStatus

from fastapi import FastAPI, APIRouter, HTTPException
from sqlalchemy.orm import defer
from starlette import status
from app.database.db_tables import db_dependency, Users
from app.models.auth_models import CreateUserRequest, Token
from auth import bcrypt_context, password_dependency, authenticate_user, create_access_token


user_router = APIRouter()

@user_router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,
                      create_user_request:CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        hashed_password=bcrypt_context.hash(create_user_request.password)
    )
    db.add(create_user_model)
    db.commit()

@user_router.post("/token", response_model=Token)
async def login_for_access_token(from_data: password_dependency,
                                 db: db_dependency):
    user = authenticate_user(from_data.username, from_data.password, db)
    if not user:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail= 'Could Not Validate User')
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}

@user_router.get("/users/", tags= ["users"])
async def read_users():
    return  [{"username": "Rick"}, {"username":"Morty"}]

@user_router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}