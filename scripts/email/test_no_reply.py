

from fastapi_mail import ConnectionConfig
from dataservice.email_service import EmailService
import asyncio


config = ConnectionConfig(
    MAIL_USERNAME="no-reply@houseofcreator.com",
    MAIL_PASSWORD="Houseofcreator#43210",
    MAIL_FROM="no-reply@houseofcreator.com",
    MAIL_PORT=465,
    MAIL_SERVER="smtppro.zoho.in",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


service = EmailService(config)

body = """
<p>Thanks for using Fastapi-mail</p> 
"""

asyncio.run(service.send_email(["rachityup@gmail.com"], "Test-Email", body))

