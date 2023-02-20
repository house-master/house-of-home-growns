from sqlalchemy.orm import Session
from datastore.sql_datastore_maker import SqlDataStoreMaker


class SqlDataStore:
    def __init__(self, connectionString: str) -> None:
        self.sessionMaker = SqlDataStoreMaker(connectionString)
        self.session: Session = self.sessionMaker.createSession()
        return

    def close(self):
        self.session.close()
