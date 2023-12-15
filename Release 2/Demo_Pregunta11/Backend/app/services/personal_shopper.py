from typing import Any
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.backend.session import DatabaseManager
from app.models.personal_shopper import PersonalShopper as PersonalShopperDB
from app.schemas.personal_shopper import PersonalShopper as PersonalShopperSchema

class PersonalShopperService:
    db = DatabaseManager()

    def create_shopper(self, shopper_data: dict[str, Any]) -> None:
        """
        Creates a new personal shopper entry in the database.
        :param shopper_data: The personal shopper data to add to the database.
        """

        with self.db.session() as session:
            with session.begin():
                shopper_db = PersonalShopperDB(
                    shopperID=shopper_data["shopperID"],
                    name=shopper_data["name"],
                )
                try:
                    session.add(shopper_db)
                    session.commit()
                except IntegrityError:
                    raise HTTPException(
                        detail=f"A personal shopper with ID '{shopper_data['shopperID']}' already exists.",
                        status_code=status.HTTP_400_BAD_REQUEST
                    )

    def create_list_shoppers(self, shoppers: list[dict[str, Any]]) -> None:
        """
        Create entries from a list of personal shoppers in the database.
        :param shoppers: The list of personal shopper items.
        """

        with self.db.session() as session:
            with session.begin():
                for shopper_data in shoppers:
                    shopper_db = PersonalShopperDB(
                        shopperID=shopper_data["shopperID"],
                        name=shopper_data["name"],
                    )
                    session.add(shopper_db)
                session.commit()

    def list_shoppers(self) -> list[dict[str, Any]]:
        """
        Get all personal shopper items from the database
        """
        with self.db.session() as session:
            with session.begin():
                statement = select(PersonalShopperDB)
                results = session.execute(statement)
                shoppers = []

                for result in results.yield_per(1000):
                    shoppers.append(PersonalShopperSchema.model_validate(result[0]).model_dump())
        return shoppers
    
    def delete_shopper(self, shopper_id: int) -> None:
        """
        Deletes a personal shopper from the database by ID.
        :param shopper_id: The ID of the personal shopper to delete.
        """
        with self.db.session() as session:
            with session.begin():
                shopper = session.query(PersonalShopperDB).filter(PersonalShopperDB.shopperID == shopper_id).first()
                if shopper:
                    session.delete(shopper)
                    session.commit()
                else:
                    raise HTTPException(
                        detail=f"Personal shopper with ID '{shopper_id}' not found.",
                        status_code=status.HTTP_404_NOT_FOUND
                    )
