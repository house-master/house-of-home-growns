from enum import Enum
from common_schema.baseModel import PydanticBaseModel

class UserRoleType(str, Enum):
    ADMIN = "ADMIN"
    PREMIUM_USER = "PREMIUM_USER"
    USER = "USER"
    PREMIUM_VENDOR = "PREMIUM_VENDOR"
    VENDOR = "VENDOR"


class UserAccountStatusType(str, Enum):
    VERIFIED = "VERIFIED"
    MOBILE_NUMBER_VERIFIED = "MOBILE_NUMBER_VERIFIED"
    VERIFICATION_PENDING = "VERIFICATION_PENDING"


class UserModel(PydanticBaseModel):
    id: str
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    roles: list[UserRoleType]
    icon: str
    account_status: UserAccountStatusType
