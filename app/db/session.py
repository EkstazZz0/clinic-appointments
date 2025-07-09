from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from app.core.config import db_connect_configuration

engine = create_engine(**db_connect_configuration)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
