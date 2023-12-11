from fastapi import FastAPI
from app.routers import router

from app.backend.session import DatabaseManager


app = FastAPI(
    title = "myPersonalShopperAPI"
)

app.on_event("startup")
async def startup() -> None:
    db = DatabaseManager()
    db.initialize_db()

app.include_router(router)
