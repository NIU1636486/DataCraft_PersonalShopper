from app.models import Base
from sqlalchemy import Column, DateTime, func, Integer, String

class Clothes(Base):
    __tablename__ = "Clothes"

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable = False)