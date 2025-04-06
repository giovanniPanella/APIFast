from fastapi import APIRouter, HTTPException, Depends
from app.schemas.enrollment import EnrollmentRequest, EnrollmentResponse
from app.database import database
from app.auth.basic_auth import get_current_username
from bson import ObjectId

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/", response_model=EnrollmentResponse)
async def create_enrollment(enrollment: EnrollmentRequest, username: str = Depends(get_current_username)):
    age_groups = []
    async for group in database.age_groups.find():
        age_groups.append(group)

    valid_group = any(group["min_age"] <= enrollment.age <= group["max_age"] for group in age_groups)
    if not valid_group:
        raise HTTPException(status_code=400, detail="Não temos grupos disponíveis para essa idade.")

    existing = await database.enrollments.find_one({"cpf": enrollment.cpf})
    if existing:
        raise HTTPException(status_code=400, detail="Já existe uma matrícula com este CPF.")

    result = await database.enrollments.insert_one(enrollment.dict())
    enrollment_response = enrollment.dict()
    enrollment_response["id"] = str(result.inserted_id)

    return enrollment_response

@router.get("/status/{cpf}", response_model=EnrollmentResponse)
async def get_enrollment_status(cpf: str, username: str = Depends(get_current_username)):
    enrollment = await database.enrollments.find_one({"cpf": cpf})
    if not enrollment:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada.")
    
    enrollment["id"] = str(enrollment["_id"])
    return EnrollmentResponse(**enrollment)
