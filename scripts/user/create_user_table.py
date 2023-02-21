import sqlalchemy
from datastore.sql_datastore import SqlDataStore
from user.datastore.user_postgres import UserPostgresDatastore
from user.domain.sql_model import DatabaseBase
from user.domain.user import UserDomainModel
from user.model.setting import Settings
import psycopg2

# conn_string = "host='localhost' dbname='ecommerce' user='postgres' password='postgres'"
# conn = psycopg2.connect(conn_string)

# setting = Settings()
datastore = UserPostgresDatastore(
    SqlDataStore(
        'postgresql+psycopg2://postgres:postgres@localhost/ecommerce'
    )
)

engine = datastore.datastore.sessionMaker.engine

DatabaseBase.metadata.create_all(engine)

print("done")
