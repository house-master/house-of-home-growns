


from typing import Any, Tuple
from common_schema.error import ErrorResponse
from common_schema.user import UserAccountStatusType, UserLoginStatusType, UserModel, UserRoleType
from user.datastore.user_postgres import UserPostgresDatastore
from user.domain.user import UserDomainModel


class UserDataService:
    def __init__(self, userDataStore: UserPostgresDatastore) -> None:
        self.userDataStore = userDataStore
        return

    def get(self, email: str) -> Tuple[UserModel, ErrorResponse]:
        user, err = self.userDataStore.get(email)
        if err != None:
            return None, err

        output = UserModel(**(user.__dict__))

        return output, None

    def create(self, user: UserModel) -> Tuple[UserModel, ErrorResponse]:
        userDomain = UserDomainModel(**user.dict())

        createdUser, err = self.userDataStore.create(userDomain)
        if err != None:
            return None, err

        output = UserModel(**(createdUser.__dict__))

        return output, None

    def update_password(self, email: str, hashed_password: str) -> Tuple[UserModel, ErrorResponse]:
        return self.__update(email, {"hashed_password": hashed_password})

    def update_name(self, email: str, first_name: str, last_name: str) -> Tuple[UserModel, ErrorResponse]:
        return self.__update(email, {"first_name": first_name, "last_name": last_name })

    def update_roles(self, email: str, roles: list[UserRoleType]) -> Tuple[list[UserRoleType], ErrorResponse]:
        return self.__update(email, {"roles": roles})

    def update_account_status(self, email: str, status: UserAccountStatusType) -> Tuple[UserModel, ErrorResponse]:
        return self.__update(email, {"account_status": status})

    def update_login_status(self, email: str, status: UserLoginStatusType) -> Tuple[UserModel, ErrorResponse]:
        return self.__update(email, {"login_status": status})

    def delete(self, email: str) -> ErrorResponse:
        return self.userDataStore.delete(email)

    def __update(self, email: str, data: dict[str, Any]) -> Tuple[UserModel, ErrorResponse]:
        user, err = self.userDataStore.get(email)
        if err != None:
            return None, err

        user, err = self.userDataStore.update(
            user, data)
        if err != None:
            return None, err

        output = UserModel(**(user.__dict__))

        return output, None
