from app.models import Base
from sqlalchemy import Column, DateTime, func, Integer, String

class Clothes(Base):
    __tablename__ = "clothes"

    id = Column(Integer, primary_key = True, autoincrement=True)
    url = Column(String, nullable = False)
    name = Column(String, nullable = False)