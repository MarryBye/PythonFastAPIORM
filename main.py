from fastapi import *
from api import router
from config import Config

app = FastAPI(debug=Config.DEBUG)
app.include_router(router)