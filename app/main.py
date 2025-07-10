from fastapi import FastAPI

from app.core.utils import lifespan
from app.endpoints.appointments import router as appointments_router
from app.endpoints.doctors import router as doctor_router

app = FastAPI(lifespan=lifespan)
app.include_router(appointments_router)
app.include_router(doctor_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
