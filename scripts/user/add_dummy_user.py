import sqlalchemy
from datastore.sql_datastore import SqlDataStore
from user.datastore.user_postgres import UserPostgresDatastore
from user.domain.user import UserDomainModel
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
    UserDomainModel(
        email="admin@houseofcreator.com",
        mobile_number="+91214344658789",
        hashed_password=hash,
        first_name="admin",
        last_name="admin",
        icon="",
        roles=["ADMIN", "PREMIUM_USER", "USER", "PREMIUM_VENDOR", "VENDOR"],
        account_status="MOBILE_NUMBER_VERIFIED",
        login_status="LOGGED_OUT",
    )
)

hash = generate_hash("password")
datastore.create(
    UserDomainModel(
        email="user@houseofcreator.com",
        mobile_number="+91214372658789",
        hashed_password=hash,
        first_name="user",
        last_name="user",
        icon="",
        roles=["PREMIUM_USER", "USER"],
        account_status="MOBILE_NUMBER_VERIFIED",
        login_status="LOGGED_OUT",
    )
)


hash = generate_hash("password")
datastore.create(
    UserDomainModel(
        email="vendor@houseofcreator.com",
        mobile_number="+912146534658789",
        hashed_password=hash,
        first_name="vendor",
        last_name="vendor",
        icon="",
        roles=["PREMIUM_VENDOR", "VENDOR"],
        account_status="MOBILE_NUMBER_VERIFIED",
        login_status="LOGGED_OUT",
    )
)

print(hash)
