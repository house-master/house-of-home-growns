import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from common_model.singleton import Singleton


class SqlDataStoreMaker(metaclass=Singleton):
    def __init__(self, connectionString: str) -> None:
        self.engine = create_engine(connectionString)
        self.sessionMaker = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)
        return

    def createSession(self) -> Session:
        return self.sessionMaker()
