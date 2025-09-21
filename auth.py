from fastapi import FastAPI, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose.constants import ALGORITHMS
from passlib.context import CryptContext
from sqlalchemy.util import deprecated

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = 'hgvfdre5tyuihjvgfdrewsdfgyu7654ewsdfgytrseaqwertyui'
ALGORITHMS = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

