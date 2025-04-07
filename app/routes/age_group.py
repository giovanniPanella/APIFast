from fastapi import APIRouter, Depends, HTTPException
from app.database import age_group_collection
from app.schemas.age_group import AgeGroupSchema, AgeGroupResponse
from app.auth.basic_auth import get_current_username
from bson import ObjectId

router = APIRouter()


#Rota para cadastar faixa etária
@router.post("/age-groups", response_model=AgeGroupResponse)
async def create_group(group: AgeGroupSchema, user: str = Depends(get_current_username)):
    result = await age_group_collection.insert_one(group.dict())
    return {**group.dict(), "id": str(result.inserted_id)}
#Rota para Verificar faixa etária
@router.get("/age-groups", response_model=list[AgeGroupResponse])
async def list_groups(user: str = Depends(get_current_username)):
    groups = []
    async for g in age_group_collection.find():
        g["id"] = str(g["_id"])
        groups.append(AgeGroupResponse(**g))
    return groups
#Rota para Deletar faixa etária
@router.delete("/age-groups/{id}")
async def delete_group(id: str, user: str = Depends(get_current_username)):
    result = await age_group_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Faixa etária não encontrada")
    return {"detail": "Faixa etária excluída com sucesso"}
