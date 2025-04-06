from pydantic import BaseModel
from typing import Optional

class AgeGroupSchema(BaseModel):
    name: str
    min_age: int
    max_age: int

class AgeGroupResponse(AgeGroupSchema):
    id: str