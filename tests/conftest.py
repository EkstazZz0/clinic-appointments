import pytest
from sqlmodel import create_engine, SQLModel, Session
from fastapi.testclient import TestClient
from fastapi import FastAPI

from app.main import app, lifespan
from app.db.session import get_session

test_engine = create_engine("sqlite:///:memory:", echo=False, connect_args={"check_same_thread": False})


@pytest.fixture(scope="session")
def init_db():
    SQLModel.metadata.create_all(test_engine)
    yield


async def override_lifespan(app: FastAPI):
    init_db()
    yield



def override_get_session():
    with Session(test_engine) as session:
        yield session


@pytest.fixture
def client(init_db):
    app.dependency_overrides[get_session] = override_get_session
    app.dependency_overrides[lifespan] = override_lifespan

    with TestClient(app=app, base_url="http://test") as c:
        yield c
    
    app.dependency_overrides.clear()
