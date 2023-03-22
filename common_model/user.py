from enum import Enum

from typing import Optional
from common_model.baseModel import PydanticBaseModel
from common_model.payment import PaymentMethodType

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
    id: Optional[int]
    email: str
    hashed_password: bytes
    first_name: str
    last_name: str
    roles: list[UserRoleType]
    icon: str
    account_status: UserAccountStatusType = UserAccountStatusType.VERIFICATION_PENDING
    login_status: UserLoginStatusType = UserLoginStatusType.LOGGED_OUT


class UserAddressType(str, Enum):
    HOME = "HOME"
    OFFICE = "OFFICE"

class UserAddressModel(PydanticBaseModel):
    id: Optional[int]
    user_id: int
    name: str
    address_type: UserAddressType
    address_line_1: str
    address_line_2: str
    landmark: Optional[str]
    city: str
    state: str
    pincode: int
    concern_person_name: str
    concern_person_number: str
    location: str


class UserPaymentDetails(PydanticBaseModel):
    id: Optional[int]
    method_type: PaymentMethodType
    name: str
    address_type: UserAddressType
    address_line_1: str
    address_line_2: str
    landmark: Optional[str]
    city: str
    state: str
    pincode: int
    concern_person_name: str
    concern_person_number: str
    location: str
