

from common_schema.baseModel import PydanticBaseModel
from dto.user import UserDTO


class AccessToken(PydanticBaseModel):
    expiry_time: int
    user: UserDTO


class RefreshToken(PydanticBaseModel):
    expiry_time: int
    user: UserDTO
