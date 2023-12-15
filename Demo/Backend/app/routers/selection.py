from fastapi import APIRouter, Path, status
from app.services.selection import SelectionService
from app.schemas.selection import Selection
router = APIRouter(prefix="/selection", tags=["selection"])


service = SelectionService()

@router.get("/")
async def get_all_selections():
    selections = service.get_selections()
    return selections


@router.get("/{userID}")
async def get_latest_selection(userID: int):
    selection = service.get_selection(userID)
    return selection

@router.post("/new_selection")
async def create_selection(selection: Selection):
    service.create_selection(selection.model_dump())

@router.put("/{selection_id}")
async def update_selection(selection_id: int, updatedSelection: Selection):
    service.update_selection(selection_id, updatedSelection.model_dump())
