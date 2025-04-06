# app/schemas/enrollment.py
from pydantic import BaseModel, Field
from typing import Optional

class EnrollmentRequest(BaseModel):
    name: str = Field(..., example="João Silva")
    cpf: str = Field(..., example="12345678900")
    age: int = Field(..., example=22)

class EnrollmentResponse(EnrollmentRequest):
    id: Optional[str] = None
