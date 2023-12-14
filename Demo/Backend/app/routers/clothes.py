from fastapi import APIRouter, Path, status
from app.services.clothes import ClothesService
from app.schemas.clothes import Clothes

router = APIRouter(prefix="/clothes", tags=["clothes (internal)"])


service = ClothesService()

@router.get("/all")
async def list_clothes():
    clothes = service.list_clothes()
    return clothes

@router.post("/")
async def new_clothes(clothes: Clothes):
    service.create_clothes(clothes.model_dump())

@router.post("/list")
async def new_clothes_list(clothes: list[Clothes]):
    service.create_list_clothes([i.model_dump() for i in clothes])

@router.delete("/{clothes_id}")
async def delete_clothes(clothes_id: int):
    service.delete_clothes(clothes_id)
    return {"message": f"Clothes item with ID {clothes_id} deleted successfully"}