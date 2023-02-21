

from datastore.sql_datastore import SqlDataStore
from user.crud.auth import AuthenticationCrud
from user.dataservice.user import UserDataService
from user.datastore.user_postgres import UserPostgresDatastore
from user.model.setting import settings



def get_auth_crud() -> AuthenticationCrud:
    try:
        sqlStore = SqlDataStore(settings.SQL_DATABASE_URL)
        userDatastore = UserPostgresDatastore(sqlStore)
        userService = UserDataService(userDatastore)
        crud = AuthenticationCrud(userService)
        yield crud
    finally:
        userDatastore.datastore.session.close()
