from fastapi import APIRouter
from app.routers.clothes import router as clothes
from app.routers.users import router as users
from app.routers.personal_shopper import router as personal_shopper

router = APIRouter()

router.include_router(clothes)
router.include_router(users)
router.include_router(personal_shopper)