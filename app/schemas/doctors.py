from sqlmodel import SQLModel, Field
from datetime import date

class DoctorBase(SQLModel):
    name: str = Field(max_length=150)
    birth_date: date = Field()


class DoctorCreate(DoctorBase):
    pass