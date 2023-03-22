


from typing import Optional
from common_model.baseModel import PydanticBaseModel
from common_model.user import UserAccountStatusType, UserRoleType



class UserDTO(PydanticBaseModel):
    email: str
    password: Optional[str]
    first_name: str
    last_name: str
    roles: list[UserRoleType]
    icon: str

