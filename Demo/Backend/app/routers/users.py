from fastapi import APIRouter, Path, status

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/list")
async def list_users():
    return {"users": []}