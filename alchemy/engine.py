from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import Config

engine = create_async_engine(
    f"postgresql+asyncpg://{Config.Database.USER}:{Config.Database.PASSWORD}@{Config.Database.HOST}:{Config.Database.PORT}/{Config.Database.NAME}"
)

SessionFactory = async_sessionmaker(bind=engine)