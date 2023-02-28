

import logging
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import EmailStr


class EmailService:
    def __init__(self, config: ConnectionConfig) -> None:
        self.config = config
        return
    
    async def send_email(self, recipient: list[EmailStr], subject: str, body):
        try:
            message = MessageSchema(
                subject=subject,
                recipients=recipient,
                body=body,
                subtype=MessageType.html)

            fm = FastMail(self.config)
            await fm.send_message(message)
            return True
        except Exception as e:
            logging.warning(f'EmailService::send_email_no_reply::{e}')
            return False
