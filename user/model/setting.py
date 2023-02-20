from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    SESSION_EXPIRY_TIME_SECONDS: int = 84600
    ACCESS_TOKEN_TIME_SECONDS: int = 3600
    JWT_AUTH_CODE_SECRET: str = "auisogfahiusovnisufhiuzhx"
    JWT_ACCESS_TOKEN_SECRET: str = "asudvbycfnguighsbdnviuyocmirug"

    APP_REDIRECT_URL: str

    class Config:
        env_file = ".env"
