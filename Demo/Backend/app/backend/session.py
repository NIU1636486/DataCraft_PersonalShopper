from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class DatabaseManager:
    """ 
    The database manager class follows a singleton design pattern to ensure that all 
    access to the database is done by reusing the connection pool created 
    by this object.
    """

    _instance = None

    def __new__(cls): 
        if cls._instance is None:
            # connection_url = URL.create(
            #     "mssql+pyodbc",
            #     username=DB_USER,
            #     password=DB_PASSWORD,
            #     host=DB_SERVER,
            #     port=DB_PORT,
            #     database=DB_NAME,
            #     query={
            #         "driver": "ODBC Driver 18 for SQL Server",
            #         "authentication": "ActiveDirectoryIntegrated",
            #     },
            # )
            # cls._engine = create_engine(url=connection_url, echo=True, pool_pre_ping=True)
            pass
        cls._engine = create_engine('sqlite:///test.db')
        cls.session = sessionmaker( 
            cls._engine, autocommit=False, expire_on_commit=False, class_=Session
        )

        cls._instance = super(DatabaseManager, cls).__new__(cls)

        return cls._instance 

    def initialize_db(self) -> None: 
        """ 
        Initializes the  database, creating the tables if they do not exist.
        """ 
        Base.metadata.create_all(self._engine)