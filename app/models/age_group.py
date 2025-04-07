from pydantic import BaseModel
#model para grupos etários
class AgeGroup(BaseModel):
    name: str
    min_age: int
    max_age: int