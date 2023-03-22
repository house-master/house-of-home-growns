from common_domain.sql_model import SqlDatabaseBase
from datastore.sql_datastore import SqlDataStore
from user.datastore.user_postgres import UserPostgresDatastore


datastore = UserPostgresDatastore(
    SqlDataStore(
        'postgresql+psycopg2://postgres:postgres@localhost/ecommerce'
    )
)

engine = datastore.datastore.sessionMaker.engine

SqlDatabaseBase.metadata.create_all(engine)

print("done")
