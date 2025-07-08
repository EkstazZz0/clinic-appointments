from fastapi import FastAPI

from app.endpoints.appointments import router as appointments_router
from app.endpoints.doctors import router as doctor_router
from app.db.repository import init_db

async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(appointments_router)
app.include_router(doctor_router)