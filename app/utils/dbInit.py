from sqlalchemy.orm import Session
from app.utils import schemas
from app.utils.initialUser import User
from app.repo import admins
import logging


def databaseInit(db: Session):
    logging.info("Initializing Database with Roles and Super Admin")
 # Create Role If They Don't Exist

    # Creating SuperAdmin
    admin_ = schemas.CreateAdmin(
        admin_name=User.ADMIN["admin_name"],
        email=User.ADMIN["email"],
        password=User.ADMIN["password"],
        contact=User.ADMIN["contact"])
    admins.create(admin_, db)
    logging.info("Database init Completed")
    return {"success": "Database Initialization Completed"}