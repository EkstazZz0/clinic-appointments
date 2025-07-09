from datetime import date

from sqlmodel import Field, SQLModel


class DoctorBase(SQLModel):
    name: str = Field(max_length=150)
    birth_date: date = Field()


class DoctorCreate(DoctorBase):
    pass
