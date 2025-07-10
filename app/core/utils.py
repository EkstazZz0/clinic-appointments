import os
import sys
from fastapi import FastAPI

from app.db.repository import init_db
from app.db.session import engine
from app.core.config import application_environment


async def lifespan(app: FastAPI):
    init_db()
    yield

    if application_environment == "test" or any("pytest" in arg for arg in sys.argv):
        engine.dispose()
        os.unlink("./temp.db")