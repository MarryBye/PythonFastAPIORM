from alchemy.engine import engine, SessionFactory

async def get_db_session():
    async with SessionFactory() as session:
        yield session
