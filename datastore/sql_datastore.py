from sqlalchemy.orm import Session
from datastore.sql_datastore_maker import SqlDataStoreMaker
from model.setting import Settings


class SqlDataStore:
    def __init__(self, settings: Settings) -> None:
        connectionString = "postgresql+psycopg2://" + settings.SIGNAL_DATABASE_USERNAME + ":" +\
            settings.SIGNAL_DATABASE_PASSWORD + "@" + \
            settings.SIGNAL_DATABASE_HOST + ":" + \
            settings.SIGNAL_DATABASE_PORT + "/" + \
            settings.SIGNAL_DATABASE
        self.sessionMaker = SqlDataStoreMaker(connectionString)
        self.settings = settings
        self.session: Session = self.sessionMaker.createSession()
        return

    def close(self):
        self.session.close()
