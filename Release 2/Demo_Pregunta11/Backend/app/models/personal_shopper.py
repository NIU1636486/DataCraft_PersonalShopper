from app.models import Base
from sqlalchemy import Column, DateTime, func, Integer, String

class PersonalShopper(Base):
    __tablename__ = "personal_shopper"

    shopperID = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable = False)

