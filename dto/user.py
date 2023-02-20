


from common_schema.baseModel import PydanticBaseModel
from common_schema.user import UserAccountStatusType, UserRoleModel



class UserDTO(PydanticBaseModel):
    email: str
    first_name: str
    last_name: str
    roles: list[UserRoleModel]
    icon: str
    account_status: UserAccountStatusType
