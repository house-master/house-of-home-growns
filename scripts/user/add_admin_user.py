import sqlalchemy
from datastore.sql_datastore import SqlDataStore
from user.datastore.user_postgres import UserPostgresDatastore
from user.domain.sql_model import DatabaseBase
from user.domain.user import UserDomainModel
from user.model.setting import Settings
import psycopg2

from user.utils.password_utils import generate_hash

# conn_string = "host='localhost' dbname='ecommerce' user='postgres' password='postgres'"
# conn = psycopg2.connect(conn_string)

# setting = Settings()
datastore = UserPostgresDatastore(
    SqlDataStore(
        'postgresql+psycopg2://postgres:postgres@localhost/ecommerce'
    )
)

hash = generate_hash("password")
datastore.create(
    UserDomainModel(
        email="admin@houseofcreator.com",
        mobile_number="+9121434658789",
        hashed_password=hash,
        first_name="admin",
        last_name="admin",
        icon="",
        roles=["ADMIN", "PREMIUM_USER", "USER", "PREMIUM_VENDOR", "VENDOR"],
        account_status="MOBILE_NUMBER_VERIFIED",
        login_status="LOGGED_OUT",
    )
)

print(hash)
