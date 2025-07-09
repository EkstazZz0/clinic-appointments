from datetime import datetime

from sqlmodel import Field, SQLModel


class AppointmentBase(SQLModel):
    doctor_id: int = Field(foreign_key="doctors.id")
    description: str = Field(max_length=3000)
    start_time: datetime = Field()


class AppointmentCreate(AppointmentBase):
    pass
