from argparse import Action
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, BackgroundTasks
from app.models import model
from app.utils import schemas
from datetime import datetime
from sqlalchemy import desc





def get_all(db: Session):
    attendances = db.query(model.Attendance).all()
    return attendances

def destroy(id: int, db: Session):
    attendance = db.query(model.Attendance).filter(model.Attendance.id == id).first()
    if not attendance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Attendance with id {id} not found")
    db.delete(attendance)
    db.commit()
    return attendance

def showAttendance(id: int,db: Session ):
    attendance = db.query(model.Attendance).filter(model.Attendance.participantId == id).first()
    if not attendance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Participant with the id {id} is not available")
    return attendance

def login_attendance(id: int, db: Session):
    time = (datetime.now().time())
    time_in = time.strftime("%H:%M:%S")
    print(time_in)
    

    attendance = db.query(model.Attendance).filter(model.Attendance.time_in == time_in ).filter( 
        model.Attendance.userId == id).order_by(desc(model.Attendance.attend_date)).first()
    if  attendance:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f" login attendance with the user id {id}  existed")
    else: 
        new_attendance= model.Attendance(
        time_in = time_in,
            userId=id            
             )
                                             
        db.add(new_attendance)

        db.commit()
        db.refresh(new_attendance)
        return new_attendance
        
    

# def logout_attendance(id: int, db: Session):
#     time = (datetime.now().time())
#     time_out = time.strftime("%H:%M:%S")
#     print(time_out)
    

#     attendance = db.query(model.Attendance).filter( 
#         model.Attendance.userId == id).order_by(desc(model.Attendance.attend_date)).first()
#     if  attendance.time_in is None:

#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"  user with  attendance id {id}  can not be found!")
#     else: 
#         attendance.time_out = time_out
#     db.commit()
#     db.refresh(attendance)
#     return attendance             