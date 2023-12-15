from fastapi import APIRouter
from app.services.user import UserService 
from app.schemas.user import User

router = APIRouter(prefix="/users", tags=["users (internal)"])

service = UserService()
@router.get("/all")
async def list_users():
    users = service.list_users()
    return users

@router.post("/")
async def new_user(user: User):
    service.create_user(user.dict())

@router.post("/list")
async def new_users_list(users: list[User]):
    service.create_list_users([i.dict() for i in users])

@router.delete("/{userID}")
async def delete_user(userID: int):
    service.delete_user(userID)