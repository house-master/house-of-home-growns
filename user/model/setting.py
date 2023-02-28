from pydantic import BaseSettings


class Settings(BaseSettings):
    SQL_DATABASE_URL: str

    SESSION_EXPIRY_TIME_SECONDS: int = 84600
    ACCESS_TOKEN_TIME_SECONDS: int = 3600
    VERIFICATION_TOKEN_TIME_SECONDS: int = 3600
    JWT_REFRESH_TOKEN_SECRET: str = "auisogfahiusovnisufhiuzhx"
    JWT_ACCESS_TOKEN_SECRET: str = "asudvbycfnguighsbdnviuyocmirug"
    JWT_VERIFICATION_CODE_SECRET: str = "asudvbycfnguighsbdnviuyocmirug"

    APP_REDIRECT_URL: str

    API_V1_STR: str

    NO_REPLY_EMAIL: str
    NO_REPLY_EMAIL_PASSWORD:  str

    EMAIL_VERIFICATION_CALLBACK_URL: str

    class Config:
        env_file = ".env"


settings = Settings()