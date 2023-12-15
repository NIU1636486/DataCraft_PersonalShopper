from app.models import Base
from sqlalchemy import Column, DateTime, func, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship



class Selection(Base):
    __tablename__ = "selection"

    selectionID = Column(Integer, primary_key=True)
    userID = Column(ForeignKey("user.userID"))
    shopperID = Column(ForeignKey("personal_shopper.shopperID"))
    approved = Column(String)
    selectionItems = relationship("SelectedItems", lazy="selectin", cascade="save-update, delete, delete-orphan")


class SelectedItems(Base):
    __tablename__ = "selected_items"
    selectionID = Column(ForeignKey("selection.selectionID", ondelete = "cascade"), primary_key = True)
    selectedItemID = Column(Integer, primary_key = True)
    clothesID = Column(ForeignKey("clothes.id"))    
