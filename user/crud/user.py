

import logging
from typing import Any
from fastapi import Request
from common_schema.error import ErrorCode, ErrorResponse
from common_schema.user import UserLoginStatusType
from dto.user import UserDTO, UserUpdateRequestDTO
from user.crud.auth import AuthenticationCrud
from user.dataservice.user import UserDataService
from user.model.setting import Settings


class UserCrud(AuthenticationCrud):
    def __init__(self, settings: Settings, userDataService: UserDataService) -> None:
        self.userDataService = userDataService
        self.settings = settings
        return

    def update(self, request: Request, ) -> UserDTO:
        return
    
    def create(request: Request, requestData: UserDTO) -> UserDTO:
        return

    def delete(self, request: Request, email: str) -> UserDTO:
        return
