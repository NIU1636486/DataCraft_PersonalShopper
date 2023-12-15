from typing import Any
from pydantic import BaseModel, Field, ConfigDict
from app.schemas.clothes import Clothes

class Selection(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    selectionID: int = Field()
    userID: int = Field()
    shopperID: int = Field()
    approved: str = Field() 
    clothes: list[Clothes] = Field()