
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

#model para isncrições
class EnrollmentModel(BaseModel):
    id: Optional[str] = Field(default_factory=str, alias="_id")
    name: str
    cpf: str
    age: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
