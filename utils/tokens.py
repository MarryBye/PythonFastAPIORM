from jose import jwt
from datetime import datetime, timedelta
from config import Config

def create_token(data: dict):
    payload = data.copy()
    payload.update({
        "exp": datetime.now() + timedelta(minutes=Config.JWT.ACCESS_TOKEN_EXPIRE_MINUTES)
    })
    return jwt.encode(payload, Config.JWT.SECRET_KEY, algorithm=Config.JWT.ALGORITHM)

def decode_token(token: str):
    try:
        return jwt.decode(token, Config.JWT.SECRET_KEY, algorithms=[Config.JWT.ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None