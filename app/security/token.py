from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import SecurityScopes
from app.repo import admins
from app.utils import dbConn
from sqlalchemy.orm import Session
from app.utils import config
import logging
from datetime import datetime
from app.utils.schemas import  TokenPayload

logger = logging.getLogger("uvicorn.error")

SECRET_KEY = config.settings.SECRET_KEY
ALGORITHM = config.settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = config.settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(encoded_jwt)
    return encoded_jwt


def verify_token(token: str , db: Session):
   print(token)
   try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=ALGORITHM
        )
        token_data = TokenPayload(**payload)
        print(payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
   except JWTError:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
   
   admin = admins.showAdmin(db, token_data.email)
   if admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find Admin",
        )
    

   return admin