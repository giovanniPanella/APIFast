from pydantic import BaseModel

class AgeGroup(BaseModel):
    name: str
    min_age: int
    max_age: int