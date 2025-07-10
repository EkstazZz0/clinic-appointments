import sys

from fastapi import FastAPI

from app.db.repository import init_db
from app.db.session import engine
from app.endpoints.appointments import router as appointments_router
from app.endpoints.doctors import router as doctor_router


async def lifespan(app: FastAPI):
    init_db()
    yield
    import os

    if os.environ["APP_ENV"] == "test" or any("pytest" in arg for arg in sys.argv):
        engine.dispose()
        os.unlink("./temp.db")


app = FastAPI(lifespan=lifespan)
app.include_router(appointments_router)
app.include_router(doctor_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
