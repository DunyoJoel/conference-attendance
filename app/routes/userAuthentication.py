from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.utils import schemas, dbConn
from app.security import token
from app.repo import admins


router = APIRouter(tags=['Admin-Authentication'])
get_db = dbConn.get_db

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dbConn.get_db)):
    admin= admins.authenticate(db, request)
    
    # if not admins.is_active(admin):
    #         raise HTTPException(status_code=400, detail="Inactive admin")

    access_token = token.create_access_token(data={"email": admin.email, "contact": admin.contact})
    return {
        "access_token": access_token, 
            "token_type": "bearer",
            }


