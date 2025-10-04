from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Generator, Annotated
from pathlib import Path

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)

def initialize_database():
    db_file = Path(__file__).parent/'database.db'
    if not db_file.exists():
        SQLModel.metadata.create_all(engine)


class Users(SQLModel,table=True):
    __tablename__ = 'users'
    id: int = Field(primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str

def get_db() -> Generator[Session,None,None]:
    with Session(engine) as session:
        yield session

db_dependency = Annotated[Session, Depends(get_db)]
