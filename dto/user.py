


from typing import Optional
from common_schema.baseModel import PydanticBaseModel
from common_schema.user import UserAccountStatusType, UserRoleType



class UserDTO(PydanticBaseModel):
    email: str
    first_name: str
    last_name: str
    roles: list[UserRoleType]
    icon: str
    account_status: UserAccountStatusType

