

from common_schema.baseModel import PydanticBaseModel
from common_schema.user import UserRoleType
from dto.user import UserDTO


class AccessToken(PydanticBaseModel):
    expiry_time: int
    role: UserRoleType
    user: UserDTO


class RefreshToken(PydanticBaseModel):
    expiry_time: int
    role: UserRoleType
    user: UserDTO


class VerificationToken(PydanticBaseModel):
    expiry_time: int
    email: str
