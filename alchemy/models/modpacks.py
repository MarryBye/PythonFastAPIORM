from sqlalchemy import Table, Column, Integer, String, LargeBinary, Enum, Date
from alchemy.metadata import metadata
from utils.enums import MinecraftVersionsEnum, LoadersEnum

modpacks = Table(
    "modpacks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, unique=True, nullable=False),
    Column("description", String, nullable=False),
    Column("logo", LargeBinary, nullable=False),
    Column("mc_loader", Enum(LoadersEnum), nullable=False),
    Column("mc_version", Enum(MinecraftVersionsEnum), nullable=False),
    Column("date_created", Date, nullable=False),
    Column("last_updated", Date, nullable=False),
    Column("hash_md5", String, nullable=False)
)