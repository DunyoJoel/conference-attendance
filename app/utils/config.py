import os
from typing import Optional
from pydantic import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv, find_dotenv
import secrets

load_dotenv(find_dotenv())


class settings (BaseSettings):
    PROJECT_NAME: str = "CONFERENCE ATTENDANCE SYSTEM"
    SQLALCHEMY_DATABASE_URL: str = os.environ.get("DATABASE_URL")
    ADMIN_NAME: str = os.environ.get("ADMIN_NAME")
    ADMIN_EMAIL: str = os.environ.get("ADMIN_EMAIL")
    ADMIN_PASSWORD: str = os.environ.get("ADMIN_PASSWORD")
    ADMIN_CONTACT: str = os.environ.get("ADMIN_CONTACT")

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM: str = os.environ.get("ALGORITHM")
    if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
            "postgres://", "postgresql://", 1)

    class Config:
        case_sensitive = True
        env_file = '.env'


@lru_cache()
def get_settings():
    return settings()


settings = get_settings()
