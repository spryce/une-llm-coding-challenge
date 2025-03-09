"""Configuration module to store essential configuration values."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class to store essential configuration values."""

    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    SESSION_TYPE = "filesystem"  # TODO: Change to Redis for production
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def validate(cls):
        """Validate the configuration values."""
        if not cls.SECRET_KEY:
            raise ValueError("FLASK_SECRET_KEY is not set!")
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set!")
        return cls
