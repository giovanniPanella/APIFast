from fastapi import APIRouter, HTTPException
from app.schemas.enrollment import EnrollmentRequest, EnrollmentResponse
from app.database import database
from bson import ObjectId

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

#rota pra cadastro de incricao
@router.post("/", response_model=EnrollmentResponse)
async def create_enrollment(enrollment: EnrollmentRequest):
    # Buscar grupos etários
    age_groups = []
    async for group in database.age_groups.find():
        age_groups.append(group)

    # Verifica se idade está dentro de algum grupo
    valid_group = any(group["min_age"] <= enrollment.age <= group["max_age"] for group in age_groups)
    if not valid_group:
        raise HTTPException(status_code=400, detail="Não temos grupos disponíveis para essa idade.")

    # Verifica CPF duplicado
    existing = await database.enrollments.find_one({"cpf": enrollment.cpf})
    if existing:
        raise HTTPException(status_code=400, detail="Já existe uma matrícula com este CPF.")

    # Inserir inscrição
    result = await database.enrollments.insert_one(enrollment.dict())
    enrollment_response = enrollment.dict()
    enrollment_response["id"] = str(result.inserted_id)

    return enrollment_response

# Verifica status da matrícula optei por retornar o ID e a indade apenas
@router.get("/status/{cpf}", response_model=EnrollmentResponse)
async def get_enrollment_status(cpf: str):
    enrollment = await database.enrollments.find_one({"cpf": cpf})
    if not enrollment:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada.")
    
    enrollment["id"] = str(enrollment["_id"])
    return EnrollmentResponse(**enrollment)
