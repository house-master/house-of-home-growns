from __future__ import annotations
from enum import Enum
from fastapi import HTTPException
from common_model.baseModel import PydanticBaseModel

class ErrorCode(str, Enum):
    NO_RECORDS_FOUND = "NO_RECORDS_FOUND"

    UNAUTHORIZED = "UNAUTHORIZED"

    ALREADY_VERIFIED = "ALREADY_VERIFIED"

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"

    @staticmethod
    def get_status_code(code: ErrorCode):
        if code == ErrorCode.NO_RECORDS_FOUND:
            return 404
        elif code == ErrorCode.ALREADY_VERIFIED:
            return 404
        elif code == ErrorCode.UNAUTHORIZED:
            return 401
        
        return 500


class ErrorResponse(PydanticBaseModel):
    error_code: ErrorCode
    message: str

    def raise_http_exception(self):
        raise HTTPException(
            status_code=ErrorCode.get_status_code(self.error_code),
            detail=self.message
        )
