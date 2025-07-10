import os

from fastapi import FastAPI

from app.core.config import application_environment
from app.db.repository import init_db
from app.db.session import engine


async def lifespan(app: FastAPI):
    init_db()
    yield

    if application_environment == "test":
        engine.dispose()
        os.unlink("./temp.db")
