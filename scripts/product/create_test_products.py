import sqlalchemy
from common_domain.product import ProductDomainModel
from datastore.sql_datastore import SqlDataStore
from user.datastore.user_postgres import UserPostgresDatastore
from user.model.setting import Settings
import psycopg2

from user.utils.password_utils import generate_hash


datastore = UserPostgresDatastore(
    SqlDataStore(
        'postgresql+psycopg2://postgres:postgres@localhost/ecommerce'
    )
)

hash = generate_hash("password")
datastore.create(
    ProductDomainModel(
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
