from datetime import datetime
import logging
from fastapi import HTTPException, Request
import jwt
from common_schema.error import ErrorCode, ErrorResponse
from common_schema.user import UserLoginStatusType, UserModel, UserRoleType
from dto.user import UserDTO
from user.dataservice.user import UserDataService
from user.model.jwt_token import AccessToken, RefreshToken
import user.utils.password_utils as password_utils
from user.model.setting import settings



class AuthenticationCrud:
    def __init__(self, userDataService: UserDataService) -> None:
        self.userDataService = userDataService
        self.settings = settings
        return

    def validate_access_token(self, request: Request) -> UserDTO:
        token = (request.headers["authorization"] if 'authorization' in request.headers.keys(
        ) else "").replace("Bearer ", "")
        access_token = AccessToken(**jwt.decode(
            token, self.settings.JWT_ACCESS_TOKEN_SECRET, algorithms=["HS256"]))

        # check access token expiry
        if access_token.expiry_time <= datetime.now().timestamp():
            return None

        user, err = self.userDataService.get(access_token.user.email)
        if err != None:
            err.raise_http_exception()

        if user.login_status == UserLoginStatusType.LOGGED_OUT:
            ErrorResponse(
                error_code = ErrorCode.UNAUTHORIZED,
                message=f'user logged out'
            ).raise_http_exception()

        return user

    def generate_access_token(self, request: Request) -> str:
        token = (request.headers["authorization"] if 'authorization' in request.headers.keys(
        ) else "").replace("Bearer ", "")
        refresh_token = RefreshToken(**jwt.decode(
            token, self.settings.JWT_REFRESH_TOKEN_SECRET, algorithms=["HS256"]))

        # check access token expiry
        if refresh_token.expiry_time <= datetime.now().timestamp():
            return None

        user, err = self.userDataService.get(refresh_token.user.email)
        if err != None:
            err.raise_http_exception()

        if user.login_status == UserLoginStatusType.LOGGED_OUT:
            ErrorResponse(
                error_code=ErrorCode.UNAUTHORIZED,
                message=f'user logged out'
            ).raise_http_exception()

        accessTokenData = AccessToken(
            expiry_time=datetime.now().timestamp() + self.settings.ACCESS_TOKEN_TIME_SECONDS,
            user=UserDTO(**user.dict()),
            role=refresh_token.role
        )

        access_token = jwt.encode(
            accessTokenData.dict(), self.settings.JWT_ACCESS_TOKEN_SECRET, algorithm="HS256")

        return access_token

    def register(self, user: UserDTO) -> UserDTO:
        user, err = self.userDataService.create(UserModel(**user.dict()))
        if err != None:
            err.raise_http_exception()

        return UserDTO(**user.dict())

    def login(self, email: str, password: str, role: UserRoleType) -> str:
        user, err = self.userDataService.get(email)
        if err != None:
            err.raise_http_exception()

        if not password_utils.verify(user.hashed_password, password):
            ErrorResponse(
                error_code=ErrorCode.UNAUTHORIZED,
                message=f'incorrect password'
            ).raise_http_exception()


        refreshTokenData = AccessToken(
            expiry_time=datetime.now().timestamp() + self.settings.SESSION_EXPIRY_TIME_SECONDS,
            user=UserDTO(**user.dict()),
            role=role
        )

        refresh_token = jwt.encode(
            refreshTokenData.dict(), self.settings.JWT_REFRESH_TOKEN_SECRET, algorithm="HS256")

        user, err = self.userDataService.update_login_status(
            email, UserLoginStatusType.LOGGED_IN)
        if err != None:
            err.raise_http_exception()

        return refresh_token

    def logout(self, request: Request) -> bool:
        token = (request.headers["authorization"] if 'authorization' in request.headers.keys(
        ) else "").replace("Bearer ", "")
        access_token = AccessToken(**jwt.decode(
            token, self.settings.JWT_ACCESS_TOKEN_SECRET, algorithms=["HS256"]))

        # check access token expiry
        if access_token.expiry_time <= datetime.now().timestamp():
            return None

        _, err = self.userDataService.update_login_status(
            access_token.user.email, UserLoginStatusType.LOGGED_OUT)
        if err != None:
            err.raise_http_exception()

        return True
