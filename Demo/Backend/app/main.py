from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.backend.session import DatabaseManager
from app.routers import router


app = FastAPI(
    title = "myPersonalShopperAPI"
)
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup() -> None:
    db = DatabaseManager()
    db.initialize_db()

app.include_router(router)
