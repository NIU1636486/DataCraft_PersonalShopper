from typing import Any
from pydantic import BaseModel, Field, ConfigDict

class PersonalShopper(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    shopperID: int = Field()
    name: str = Field()