from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint
from alchemy.metadata import metadata

modpack_tags = Table(
    "modpack_tags",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("modpack_id", Integer, ForeignKey("modpacks.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tags.id"), nullable=False),
    UniqueConstraint("modpack_id", "tag_id", name="uq_modpack_tag")
)