

from common_schema.error import ErrorResponse


class UserVerificationService:
    def __init__(self) -> None:
        return

    def send_verification_email(email: str) -> ErrorResponse:
        return

    def verify_email_token(token: str) -> ErrorResponse:
        return

    def send_verification_sms(mobile_number: str) -> ErrorResponse:
        return

    def verify_sms_token(token: str) -> ErrorResponse:
        return
