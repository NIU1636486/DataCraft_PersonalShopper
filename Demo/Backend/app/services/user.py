from typing import Any
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.backend.session import DatabaseManager
from app.models.user import User as UserDB
from app.schemas.user import User

class UserService:
    db = DatabaseManager()

    def create_user(self, user_data: dict[str, Any]) -> None:
        """
        Creates a new user entry in the database.
        :param user_data: The user data to add to the database.
        """

        with self.db.session() as session:
            with session.begin():
                user_db = UserDB(
                    userID=user_data["userID"],
                    username=user_data["username"],
                )
                try:
                    session.add(user_db)
                    session.commit()
                except IntegrityError:
                    raise HTTPException(
                        detail=f"A user with ID '{user_data['userID']}' already exists.",
                        status_code=status.HTTP_400_BAD_REQUEST
                    )

    def create_list_users(self, users: list[dict[str, Any]]) -> None:
        """
        Create entries from a list of users in the database.
        :param users: The list of user items.
        """

        with self.db.session() as session:
            with session.begin():
                for user_data in users:
                    user_db = UserDB(
                        userID=user_data["userID"],
                        username=user_data["username"],
                    )
                    session.add(user_db)
                session.commit()

    def list_users(self) -> list[dict[str, Any]]:
        """
        Get all user items from the database
        """
        with self.db.session() as session:
            with session.begin():
                statement = select(UserDB)
                results = session.execute(statement)
                users = []

                for result in results.yield_per(1000):
                    print(result)
                    users.append(User.model_validate(result[0]).model_dump())
        return users
    

    def delete_user(self, user_id: int) -> None:
        """
        Deletes a user from the database by ID.
        :param user_id: The ID of the user to delete.
        """
        with self.db.session() as session:
            with session.begin():
                user = session.query(UserDB).filter(UserDB.userID == user_id).first()
                if user:
                    session.delete(user)
                    session.commit()
                else:
                    raise HTTPException(
                        detail=f"User with ID '{user_id}' not found.",
                        status_code=status.HTTP_404_NOT_FOUND)
