from sqlalchemy import Table, Column, Integer, String
from alchemy.metadata import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("login", String, unique=True, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("firstname", String, nullable=False),
    Column("lastname", String, nullable=False),
    Column("nickname", String, nullable=False),
    Column("email", String, unique=True, nullable=False)
)