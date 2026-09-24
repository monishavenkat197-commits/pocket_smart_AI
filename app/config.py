from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "PocketSmart AI"

    secret_key: str = "change-me"

    database_url: str = "sqlite:///./pocketsmart.db"

    gemini_api_key: str = ""

    gemini_model: str = "gemini-2.5-flash"

    cookie_secure: bool = False

    max_upload_mb: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()