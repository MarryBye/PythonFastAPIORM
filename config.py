from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.dev")

class Config:
    DEBUG = True

    class Database:
        USER = getenv("DB_USER", "your_user")
        PASSWORD = getenv("DB_PASSWORD", "your_password")
        HOST = getenv("DB_HOST", "localhost")
        PORT = getenv("DB_PORT", 5432)
        NAME = getenv("DB_NAME", "your_db_name")

    class JWT:
        SECRET_KEY = getenv("JWT_SECRET_KEY", "your_secret_key")
        ALGORITHM = getenv("JWT_ALGORITHM", "HS256")
        ACCESS_TOKEN_EXPIRE_MINUTES = getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30)
        REFRESH_TOKEN_EXPIRE_MINUTES = getenv("JWT_REFRESH_TOKEN_EXPIRE_MINUTES", 60)