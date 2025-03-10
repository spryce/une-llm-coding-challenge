"""Configuration module to store essential configuration values."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class to store essential configuration values."""

    # Future versions may persist user sessions to db so we use a persistant key also
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    # TODO: Change SESSION_TYPE to Redis for production
    SESSION_TYPE = "filesystem"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @classmethod
    def validate(cls):
        """Validate the configuration values and return cls."""
        if not cls.SECRET_KEY:
            raise ValueError("FLASK_SECRET_KEY is not set!")
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set!")
        return cls
