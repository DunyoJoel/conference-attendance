from fastapi import FastAPI,Depends
from app.utils.config import  settings
from app.utils.dbInit import databaseInit
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app.utils import dbConn
from app.routes import  userAuthentication, userActivities


app = FastAPI(
    title = settings.PROJECT_NAME
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
get_db = dbConn.get_db

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/db-startup")
async def dbSetup(db: Session = Depends(get_db)):
    return databaseInit(db)


app.include_router(userAuthentication.router)
app.include_router(userActivities.router)