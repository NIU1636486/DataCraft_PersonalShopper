from fastapi import APIRouter
from app.services.personal_shopper import PersonalShopperService  # Update the import path based on your project structure
from app.schemas.personal_shopper import PersonalShopper  # Update the import path based on your project structure

router = APIRouter(prefix="/personal_shoppers", tags=["personal_shoppers (internal)"])

service = PersonalShopperService()  # Assuming you have a PersonalShopperService class in app/services/personal_shopper.py

@router.get("/all")
async def list_shoppers():
    shoppers = service.list_shoppers()
    return shoppers

@router.post("/")
async def new_shopper(shopper: PersonalShopper):
    service.create_shopper(shopper.dict())

@router.post("/list")
async def new_shoppers_list(shoppers: list[PersonalShopper]):
    service.create_list_shoppers([i.dict() for i in shoppers])

@router.delete("/{shopper_id}")
async def delete_shopper(shopper_id: int):
    service.delete_shopper(shopper_id)