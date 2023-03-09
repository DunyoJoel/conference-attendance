from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from app.security import token
from sqlalchemy.orm import Session
from app.utils import dbConn

from fastapi.security import SecurityScopes
from app.repo import admins

get_db = dbConn.get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login",  scheme_name="JWT" )
          

async def get_current_user(data: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    
    return token.verify_token(data, db)

def get_current_active_user(
    current_admin = Security(get_current_user)):
    # if not admins.is_active(current_admin):
    #     raise HTTPException(status_code=400, detail="Inactive admin")
     return current_admin