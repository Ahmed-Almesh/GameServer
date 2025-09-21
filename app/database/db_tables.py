from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Generator, Annotated

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)

class Users(SQLModel,table=True):
    id = Field(primary_key=True)
    username: str = Field(index=True)

def get_db() -> Generator[Session,None,None]:
    with Session(engine) as session:
        yield session

db_dependancy = Annotated[Session, Depends(get_db)]
