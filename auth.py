from datetime import timedelta, datetime
from http.client import HTTPException
from os.path import defpath
from typing import Annotated

from dns.dnssecalgs import algorithms
from jose import jwt, JWTError
from sqlmodel import Session, select
from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose.constants import ALGORITHMS
from passlib.context import CryptContext

from sqlalchemy.util import deprecated
from starlette import status

from app.database.db_tables import Users

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = 'hgvfdre5tyuihjvgfdrewsdfgyu7654ewsdfgytrseaqwertyui'
ALGORITHMS = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

password_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]

def authenticate_user(username: str, password: str, db: Session):
    user = db.exec(select(Users).where(Users.username == username)).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.now() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode,SECRET_KEY, algorithm=ALGORITHMS)

async def get_current_user(token:Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHMS])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')