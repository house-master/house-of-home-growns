from datetime import datetime
import logging
from fastapi import BackgroundTasks, HTTPException, Request
from fastapi_mail import ConnectionConfig
import jwt
from common_schema.error import ErrorCode, ErrorResponse
from common_schema.user import UserAccountStatusType, UserLoginStatusType, UserModel, UserRoleType
from dataservice.email_service import EmailService
from dto.user import UserDTO
from user.dataservice.user import UserDataService
from user.model.jwt_token import AccessToken, RefreshToken, VerificationToken
import user.utils.password_utils as password_utils
from user.model.setting import settings



class AuthenticationCrud:
    def __init__(self, userDataService: UserDataService) -> None:
        self.userDataService = userDataService
        self.email_service = EmailService(ConnectionConfig(
            MAIL_USERNAME=settings.NO_REPLY_EMAIL,
            MAIL_PASSWORD=settings.NO_REPLY_EMAIL_PASSWORD,
            MAIL_FROM=settings.NO_REPLY_EMAIL,
            MAIL_PORT=465,
            MAIL_SERVER="smtppro.zoho.in",
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=True,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True
        ))
        return

    def validate_access_token(self, request: Request) -> UserDTO:
        token = (request.headers["authorization"] if 'authorization' in request.headers.keys(
        ) else "").replace("Bearer ", "")
        access_token = AccessToken(**jwt.decode(
            token, settings.JWT_ACCESS_TOKEN_SECRET, algorithms=["HS256"]))

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
            token, settings.JWT_REFRESH_TOKEN_SECRET, algorithms=["HS256"]))

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
            expiry_time=datetime.now().timestamp() + settings.ACCESS_TOKEN_TIME_SECONDS,
            user=UserDTO(**user.dict()),
            role=refresh_token.role
        )

        access_token = jwt.encode(
            accessTokenData.dict(), settings.JWT_ACCESS_TOKEN_SECRET, algorithm="HS256")

        return access_token

    def register(self, user: UserDTO, background_tasks: BackgroundTasks) -> UserDTO:
        hashed_password = password_utils.generate_hash(user.password)
        user_model = UserModel(**user.dict(), hashed_password=hashed_password)
        user_model.account_status = UserAccountStatusType.VERIFICATION_PENDING
        user, err = self.userDataService.create(user_model)
        if err != None:
            err.raise_http_exception()

        err = self.send_verification_email(user.email, background_tasks)
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
            expiry_time=datetime.now().timestamp() + settings.SESSION_EXPIRY_TIME_SECONDS,
            user=UserDTO(**user.dict()),
            role=role
        )

        refresh_token = jwt.encode(
            refreshTokenData.dict(), settings.JWT_REFRESH_TOKEN_SECRET, algorithm="HS256")

        user, err = self.userDataService.update_login_status(
            email, UserLoginStatusType.LOGGED_IN)
        if err != None:
            err.raise_http_exception()

        return refresh_token

    def logout(self, request: Request) -> bool:
        token = (request.headers["authorization"] if 'authorization' in request.headers.keys(
        ) else "").replace("Bearer ", "")
        access_token = AccessToken(**jwt.decode(
            token, settings.JWT_ACCESS_TOKEN_SECRET, algorithms=["HS256"]))

        # check access token expiry
        if access_token.expiry_time <= datetime.now().timestamp():
            return None

        _, err = self.userDataService.update_login_status(
            access_token.user.email, UserLoginStatusType.LOGGED_OUT)
        if err != None:
            err.raise_http_exception()

        return True

    def send_verification_email(self, email: str, background_tasks: BackgroundTasks) -> ErrorResponse:
        verificationTokenData = VerificationToken(
            expiry_time=datetime.now().timestamp() + settings.VERIFICATION_TOKEN_TIME_SECONDS,
            email=email
        )

        verification_token = jwt.encode(
            verificationTokenData.dict(), settings.JWT_VERIFICATION_CODE_SECRET, algorithm="HS256")

        url = settings.EMAIL_VERIFICATION_CALLBACK_URL + \
            f'?token={verification_token}'

        background_tasks.add_task(
            self.email_service.send_email, recipient=[email], subject="Verify Email", body=f'<p>Verification url - {url}</p>')

        return

    def verify_email_token(self, token: str) -> ErrorResponse:
        verification_token = VerificationToken(**jwt.decode(
            token, settings.JWT_VERIFICATION_CODE_SECRET, algorithms=["HS256"]))

        # check access token expiry
        if verification_token.expiry_time <= datetime.now().timestamp():
            return None

        user, err = self.userDataService.get(verification_token.email)
        if err != None:
            err.raise_http_exception()

        if user.account_status != UserAccountStatusType.VERIFICATION_PENDING:
            ErrorResponse(
                error_code=ErrorCode.ALREADY_VERIFIED,
                message=f'user email already verified'
            ).raise_http_exception()

        user, err = self.userDataService.update_account_status(
            user.email, UserAccountStatusType.EMAIL_VERIFIED)
        if err != None:
            err.raise_http_exception()

        return
