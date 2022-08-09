from typing import List

from leanapi.config import ApiConfig


class AppConfig(ApiConfig):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

    NAME: str = "melisa"
    DESCRIPTION: str = ""
    VERSION: str = "1.0.0"
    BASE_URL: str = "/melisa_service"
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    class Config:
        case_sensitive = True

    @classmethod
    def load(cls):
        return cls()