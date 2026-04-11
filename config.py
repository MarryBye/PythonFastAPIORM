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