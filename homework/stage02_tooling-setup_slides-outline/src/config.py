import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

def get_key(key_name: str) -> str:
    """Get a secret key from environment variables."""
    return os.getenv(key_name)