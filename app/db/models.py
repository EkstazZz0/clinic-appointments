from datetime import date, datetime

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class Doctor(SQLModel, table=True):
    __tablename__ = "doctors"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=150)
    birth_date: date = Field()


class Appointment(SQLModel, table=True):
    __tablename__ = "appointments"

    id: int | None = Field(default=None, primary_key=True)
    doctor_id: int = Field(foreign_key="doctors.id")
    description: str = Field(max_length=3000)
    start_time: datetime = Field()

    __table_args__ = (
        UniqueConstraint("doctor_id", "start_time", name="unique_doctor_start_time"),
        None,
    )
