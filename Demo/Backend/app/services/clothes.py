from typing import Any
from fastapi import HTTPException,status
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from app.backend.session import DatabaseManager
from app.models.clothes import Clothes as ClothesDB
from app.schemas.clothes import Clothes


class ClothesService:
    db = DatabaseManager()

    def create_clothes(self, clothes: dict[int, Any]) -> None:
        """
        Creates a new entry of clothes in the database.
        :param clothes: The item of clothing to add to the database.
        """

        with self.db.session() as session:
            with session.begin():
                clothes_db = ClothesDB(
                    id = clothes["id"],
                    name = clothes["name"],
                    url = clothes["url"]
                )
                try:
                    session.add(clothes_db)
                    session.commit()
                except IntegrityError:
                    raise HTTPException(
                        detail = f"""A clothes item with id '{clothes["id"]}' already exists.""",
                        status_code = status.HTTP_400_BAD_REQUEST
                    )
    
    def create_list_clothes(self, clothes:list[dict[id, Any]]):
        """
        Create entries from a list of clothes in the database.
        :param clothes: The list of clothes items.
        """

        with self.db.session() as session:
            with session.begin():
                for i in clothes:
                    clothes_db = ClothesDB(
                    id = i["id"],
                    name = i["name"],
                    url = i["url"]
                    )
                    session.add(clothes_db)
                session.commit()


    def list_clothes(self) -> list[dict[int, Any]]:
        """
        Get all clothe items from the database
        """
        with self.db.session() as session:
            with session.begin():
                statement = select(ClothesDB)
                results = session.execute(statement)
                clothes = []

                for result in results.yield_per(1000):
                    clothes.append(Clothes.model_validate(result[0]).model_dump())
        return clothes

    def get_clothe(self, clothe_id):
        with self.db.session() as session:
            with session.begin():
                statement = select(ClothesDB).where(ClothesDB.id == clothe_id)
                result = session.execute(statement)
                result = [i for i in result]
                clothe = result[0]
                if clothe is None:
                    raise HTTPException(
                        detail="Not exist",
                        status_code = status.HTTP_404_NOT_FOUND
                    )
            return Clothes.model_validate(clothe[0]).model_dump()
    def delete_clothes(self, clothes_id: int) -> None:
        """
        Deletes a clothes item from the database by ID.
        :param clothes_id: The ID of the clothes item to delete.
        """
        with self.db.session() as session:
            with session.begin():
                clothes = session.query(ClothesDB).filter(ClothesDB.id == clothes_id).first()
                if clothes:
                    session.delete(clothes)
                    session.commit()
                else:
                    raise HTTPException(
                        detail=f"Clothes item with ID '{clothes_id}' not found.",
                        status_code=status.HTTP_404_NOT_FOUND
                    )