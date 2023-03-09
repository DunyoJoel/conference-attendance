from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model 
from app.utils import schemas


def create(request: schemas.CreateAdmin, db: Session):
    admin = db.query(model.Admin).filter(model.Admin.email == request.email).first()
    if admin:
        raise HTTPException(status_code= 303,
                            detail =f"Admin with the name { request.email} already exist")
    else: 
        new_admin = model.Admin(admin_name =request.admin_name,
                              contact = request.contact,
                              email= request.email,
                              password= Hash.bcrypt(request.password),
                              
                             
                              )
                              
                              
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
    
def create_new_admin(request: schemas.CreateAdmin, db: Session,current_user):
    admin = db.query(model.Admin).filter(model.Admin.email == request.email).first()
    if admin:
        raise HTTPException(status_code= 303,
                            detail =f"Admin with the name { request.email} already exist")
    else: 
        new_admin = model.Admin(admin_name =request.admin_name,
                              contact = request.contact,
                              email= request.email,
                              password= Hash.bcrypt(request.password),
                              
                             
                              )
                              
                              
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
        



def show(id: int, db: Session):
    admin = db.query(model.Admin).filter(model.Admin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admin with the id {id} is not available")
    return admin

# def showLoginUser(current_user, db: Session):
#     loginUser =db.query(model.User, model.Sensor).outerjoin(model.Sensor).filter(model.User.id == current_user.id).first()
#     if not loginUser:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return loginUser
  

def get_all(db: Session):
    admin= db.query(model.User).filter(model.Admin.action_by == None).all()
    return admin

def get_all_admin(db: Session):
    admin = db.query(model.Admin).filter(model.Admin.action_by is not None).all()
    return admin

def destroy(id: int, db: Session):
    admin = db.query(model.Admin).filter(model.Admin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    db.delete(admin)
    db.commit()
    return admin


def update(id: int, request: schemas.ShowAdmin, db: Session):
    admin = db.query(model.Admin).filter(model.Admin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    admin.admin_name =request.admin_name
    admin.contact = request.contact
    admin.email = request.email
    admin.password = request.password
    admin.date = request.dateAdded

    db.commit()
    db.refresh(admin)
    return admin



def showAdmin(db: Session, email: str ):
    admin = db.query(model.Admin).filter(model.Admin.email == email).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admin with the id {email} is not available")
    return admin
def get_by_name(contact: str, db: Session):
    admin = db.query(model.Admin).filter(
        model.Admin.contact == contact).first()
    return admin



# def is_active(user: schemas.ShowAdmin) -> bool:
#         return user.isActive
    
def get_by_email(db: Session, request):
    admin = db.query(model.Admin).filter(model.Admin.email ==request).first()
    return admin

def authenticate( db: Session ,request):
        admin = get_by_email(db, request.username)
        if not admin:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
        elif not Hash.verify(admin.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
        return admin