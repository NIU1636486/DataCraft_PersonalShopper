from fastapi import APIRouter
from app.routers.users import router as users

router = APIRouter()

router.include_router(users)