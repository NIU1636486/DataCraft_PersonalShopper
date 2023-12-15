from typing import Any
from fastapi import HTTPException, status
from sqlalchemy import select, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from app.backend.session import DatabaseManager
from app.models.selection import SelectedItems
from app.models.selection import Selection as SelectionDB
from app.models.clothes import Clothes as ClothesDB
from app.schemas.clothes import Clothes
from app.schemas.selection import Selection
from app.services.clothes import ClothesService

class SelectionService:
    db = DatabaseManager()


    def create_selection(self, selection_data: dict[int, Any]):
        with self.db.session() as session:
            with session.begin():
                selectedItems = []
                for index , clothe in enumerate(selection_data.get("clothes", [])):
                    selectedItem = SelectedItems(
                        selectedItemID = index,
                        clothesID = clothe["id"]
                    )
                    selectedItems.append(selectedItem)

                selection = SelectionDB(
                    selectionID = selection_data["selectionID"],
                    userID = selection_data["userID"],
                    shopperID = selection_data["shopperID"],
                    approved = "Waiting",
                    selectionItems = selectedItems
                )
                print(selection.__dict__)
                try:
                    session.add(selection)
                    session.commit()
                except IntegrityError:
                    raise HTTPException(
                        detail= "Ja existeix",
                        status_code = status.HTTP_400_BAD_REQUEST
                    )
    
    def get_selections(self):
        service = ClothesService()
        with self.db.session() as session:
            selections = (
                session.query(SelectionDB)
                .options(joinedload(SelectionDB.selectionItems))
                .all()
            )

            result = []
            for selection in selections:
                selection_data = selection.__dict__
                clothes = []

                for selected_item in selection_data["selectionItems"]:
                    clothe = service.get_clothe(selected_item.clothesID)
                    clothes.append(clothe)

                selection_model = Selection(
                    selectionID=selection_data["selectionID"],
                    userID=selection_data["userID"],
                    shopperID=selection_data["shopperID"],
                    approved = selection_data["approved"],
                    clothes=clothes,
                )

                result.append(selection_model)

        return result

    def get_selection(self, user_id):
        service = ClothesService()
        with self.db.session() as session:
            latest_selection = (
                session.query(SelectionDB)
                .filter_by(userID=user_id)
                .order_by(desc(SelectionDB.selectionID))
                .options(joinedload(SelectionDB.selectionItems))
                .first()
            )
            selection_data = latest_selection.__dict__
            clothes = []

            for selected_item in selection_data["selectionItems"]:
                clothe = service.get_clothe(selected_item.clothesID)
                clothes.append(clothe)

            selection_model = Selection(
                selectionID=selection_data["selectionID"],
                userID=selection_data["userID"],
                shopperID=selection_data["shopperID"],
                approved = selection_data["approved"],
                clothes=clothes,
            )

        return selection_model
    
    def update_selection(self, selection_id, updated_selection):
        with self.db.session() as session:
            with session.begin():
                # Retrieve the selection to be updated
                selection_to_update = (
                    session.query(SelectionDB)
                    .filter_by(selectionID=selection_id)
                    .options(joinedload(SelectionDB.selectionItems))
                    .one()
                )

                # Update the selection data
                selection_to_update.userID = updated_selection["userID"]
                selection_to_update.shopperID = updated_selection["shopperID"]
                selection_to_update.approved = updated_selection["approved"]

                # Clear existing selected items
                selection_to_update.selectionItems.clear()

                # Add new selected items
                selected_items = []
                for index, clothe in enumerate(updated_selection.get("clothes", [])):
                    selected_item = SelectedItems(
                        selectedItemID=index,
                        clothesID=clothe["id"]
                    )
                    selected_items.append(selected_item)

                selection_to_update.selectionItems = selected_items

                session.commit()
