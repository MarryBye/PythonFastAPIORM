from sqlalchemy import Table, Column, Integer, String, Enum
from alchemy.metadata import metadata
from utils.enums import TagsEnum

tags = Table(
    "tags",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Enum(TagsEnum), nullable=False),
    Column("color", String, nullable=False)
)