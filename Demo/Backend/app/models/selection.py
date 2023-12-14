from app.models import Base
from sqlalchemy import Column, DateTime, func, Integer, String
from sqlalchemy.orm import relationship



class Selection(Base):
    __tablename__ = "selection"

    id: Column(Integer, primary_key=True)
    UserID: Column(Integer, ForeignKey("user.UserID"))
