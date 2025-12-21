
from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone
from shared_lib.config.setting import get_settings

class JWTAuth: 

    @staticmethod
    def create_access_token(data: dict, expires_delta: int = 30): 
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, get_settings().JWT_SECRET_KEY, algorithm=get_settings().JWT_ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def verify_token(token: str): 
        try: 
            payload = jwt.decode(token, get_settings().JWT_SECRET_KEY, algorithms=[get_settings().JWT_ALGORITHM])
            return payload
        except jwt.JWTError:
            raise 
