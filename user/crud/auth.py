

from datetime import datetime
import logging
from typing import Optional
from fastapi import Request
import jwt
from dto.user import UserDTO
from user.datastore.roles_postgres import UserRolesPostgresDataService
from user.datastore.user_postgres import UserPostgresDataService
from user.model.jwt_token import AccessToken
from user.model.setting import Settings


class AuthenticationCrud:
    def __init__(self, settings: Settings, userDataService: UserPostgresDataService, userRoleService: UserRolesPostgresDataService) -> None:
        self.userDataService = userDataService
        self.userRoleService = userRoleService
        self.settings = settings
        return

    def validateAccessToken(self, request: Request, role: str) -> Optional[UserDTO]:
        try:
            token = (request.headers["authorization"] if 'authorization' in request.headers.keys(
            ) else "").replace("Bearer ", "")
            data = AccessToken(**jwt.decode(
                token, self.settings.JWT_ACCESS_TOKEN_SECRET, algorithms=["HS256"]))

            # check access token expiry
            if data.expiry_time <= datetime.now().timestamp():
                return None

            user = self.userDataService.getUserByEmail(data.user.email)

            if user == None or not user.login_state:
                return None

            return user
        except Exception as e:
            logging.warning(
                f'AuthenticationCrud -- validateAccessToken --> Some error in validating access token')
            logging.warning(e)
            return None

    def generateAccessToken(self, request: Request, role: str) -> Optional[UserDTO]:
        try:
            token = (request.headers["authorization"] if 'authorization' in request.headers.keys(
            ) else "").replace("Bearer ", "")
            data = JwdTokenDataType(**jwt.decode(
                token, self.settings.JWT_ACCESS_TOKEN_SECRET, algorithms=["HS256"]))

            # check access token expiry
            if data.expiry_time <= datetime.now().timestamp():
                return None

            user = self.userDataService.getUserByEmail(data.user.email)

            if user == None or not user.login_state:
                return None

            return user
        except Exception as e:
            logging.warning(
                f'AuthenticationCrud -- validateAccessToken --> Some error in validating access token')
            logging.warning(e)
            return None

    def register(self, request: Request) -> Optional[str]:
        try:
            authCode = (request.headers["authorization"] if 'authorization' in request.headers.keys(
            ) else "").replace("Bearer ", "")
            data = JwdTokenDataType(**jwt.decode(
                authCode, self.settings.JWT_AUTH_CODE_SECRET, algorithms=["HS256"]))

            # check auth code expiry
            if data.expiry_time <= datetime.now().timestamp():
                return None

            accessTokenData = JwdTokenDataType(
                expiry_time=datetime.now().timestamp() + self.settings.ACCESS_TOKEN_TIME_SECONDS,
                user=data.user
            )

            access_token = jwt.encode(
                accessTokenData.dict(), self.settings.JWT_ACCESS_TOKEN_SECRET, algorithm="HS256")

            updatesUser = self.userDataService.updateLoginState(
                data.user.email, True)
            if updatesUser == None:
                return None

            return access_token
        except Exception as e:
            logging.warning(
                f'AuthenticationCrud -- login --> Some error generating access token')
            logging.warning(e)
            return None

    def login(self, request: Request) -> Optional[str]:
        try:
            authCode = (request.headers["authorization"] if 'authorization' in request.headers.keys(
            ) else "").replace("Bearer ", "")
            data = JwdTokenDataType(**jwt.decode(
                authCode, self.settings.JWT_AUTH_CODE_SECRET, algorithms=["HS256"]))

            # check auth code expiry
            if data.expiry_time <= datetime.now().timestamp():
                return None

            accessTokenData = JwdTokenDataType(
                expiry_time=datetime.now().timestamp() + self.settings.ACCESS_TOKEN_TIME_SECONDS,
                user=data.user
            )

            access_token = jwt.encode(
                accessTokenData.dict(), self.settings.JWT_ACCESS_TOKEN_SECRET, algorithm="HS256")

            updatesUser = self.userDataService.updateLoginState(
                data.user.email, True)
            if updatesUser == None:
                return None

            return access_token
        except Exception as e:
            logging.warning(
                f'AuthenticationCrud -- login --> Some error generating access token')
            logging.warning(e)
            return None


    def logout(self, request: Request) -> bool:
        user = self.validateAccessToken(request, "logout")
        if user == None:
            return False

        updatesUser = self.userDataService.updateLoginState(user.email, False)
        if updatesUser == None:
            return False
