from pydantic import BaseModel
from pydantic.fields import Field


class Employer(BaseModel):
    name: str | None


class Metro(BaseModel):
    station_name: str | None
    line_name: str | None


class Address(BaseModel):
    city: str | None
    street: str | None
    building: str | None
    metro: Metro | None


class Salary(BaseModel):
    from_: int | None = Field(alias='from')
    to: int | None
    currency: str | None


