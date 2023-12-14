from typing import Any
from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    userID: int = Field()
    username: str = Field()