from fastapi import FastAPI

from app.backend.session import DatabaseManager
from app.routers import router


app = FastAPI(
    title = "myPersonalShopperAPI"
)

@app.on_event("startup")
async def startup() -> None:
    db = DatabaseManager()
    db.initialize_db()

app.include_router(router)
