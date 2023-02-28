from enum import Enum

from typing import Optional
from common_schema.baseModel import PydanticBaseModel

class UserRoleType(str, Enum):
    ADMIN = "ADMIN"
    PREMIUM_USER = "PREMIUM_USER"
    USER = "USER"
    PREMIUM_VENDOR = "PREMIUM_VENDOR"
    VENDOR = "VENDOR"


class UserAccountStatusType(str, Enum):
    EMAIL_VERIFIED = "EMAIL_VERIFIED"
    MOBILE_NUMBER_VERIFIED = "MOBILE_NUMBER_VERIFIED"
    VERIFICATION_PENDING = "VERIFICATION_PENDING"


class UserLoginStatusType(str, Enum):
    LOGGED_IN = "LOGGED_IN"
    LOGGED_OUT = "LOGGED_OUT"


class UserModel(PydanticBaseModel):
    id: Optional[str]
    email: str
    hashed_password: bytes
    first_name: str
    last_name: str
    roles: list[UserRoleType]
    icon: str
    account_status: UserAccountStatusType = UserAccountStatusType.VERIFICATION_PENDING
    login_status: UserLoginStatusType = UserLoginStatusType.LOGGED_OUT
