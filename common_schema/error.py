

from enum import Enum
from common_schema.baseModel import PydanticBaseModel

class ErrorCode(str, Enum):
    NO_RECORDS_FOUND = "NO_RECORDS_FOUND"

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"

class ErrorResponse(PydanticBaseModel):
    error_code: ErrorCode
    message: str
