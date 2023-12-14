from app.models import Base
from sqlalchemy import Column, DateTime, func, Integer, String

class User(Base):
    __tablename__ = "user"

    userID = Column(Integer, primary_key = True, autoincrement=True)
    username = Column(String, nullable = False)

