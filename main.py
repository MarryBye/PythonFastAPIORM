from fastapi import *
from api import router

from alchemy.engine import engine
from alchemy.metadata import metadata
from alchemy.models import *

from config import Config

app = FastAPI(debug=Config.DEBUG)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

app.include_router(router)