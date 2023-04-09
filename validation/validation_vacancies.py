from pydantic import BaseModel
from validation.validation_utils import Salary, Address, Employer


class Vacancies(BaseModel):
    name: str | None
    employer: Employer | None
    salary: Salary | None
    address: Address | None
    alternate_url: str | None
    published_at: str | None
