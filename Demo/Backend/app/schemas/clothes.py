from typing import Any
from pydantic import BaseModel, Field, ConfigDict


class Clothes(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field()
    url: str = Field()
    name: str = Field()