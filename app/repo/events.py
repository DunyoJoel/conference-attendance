from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model 
from app.utils import schemas
from datetime import datetime
from sqlalchemy import desc
import hashlib

def create(request: schemas.CreateEvent, db: Session, current_user):
    event = db.query(model.Event).filter(model.Event.event_name  == request.event_name ).first()
    if event:
        raise HTTPException(status_code= 303,
                            detail =f"Event  with the event name { request.event_name} already exist")
    else: 
        new_event = model.Event(event_name =request.event_name,
                                venue = request.venue,
                                start_date = request.start_date,
                                end_date = request.end_date,
                                number_of_participants = request.number_of_participants,
                                description = request.description,
                               admin_id  = current_user.id 
                              )
                              
                              
        db.add(new_event)
        db.commit()
        db.refresh(new_event)
        return new_event
    




def show(id: int, db: Session):
    event = db.query(model.Event).filter(model.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with the id {id} is not available")
    return event

# def showLoginUser(current_user, db: Session):
#     loginUser =db.query(model.User, model.Sensor).outerjoin(model.Sensor).filter(model.User.id == current_user.id).first()
#     if not loginUser:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return loginUser
  

def get_all(db: Session):
    events = db.query(model.Event,model.Admin).outerjoin(model.Admin).all()
    print(events)

    return events



def destroy(id: int, db: Session):
    event = db.query(model.Event).filter(model.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"event with id {id} not found")
    db.delete(event)
    db.commit()
    return event


def update(id: int, request: schemas.UpdateEvent, db: Session):
    event = db.query(model.Event).filter(model.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"departments with id {id} not found")

    event.event_name =request.event_name
    event.venue = request.venue
    event.start_date = request.start_date
    event.end_date = request.end_date
    event.number_of_participants = request.number_of_participants
    event.description = request.description

    
    db.commit()
    db.refresh(event)
    return event



def showEvent(db: Session, event_name: str ):
    event = db.query(model.Event).filter(model.Event.event_name == event_name).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id {event_name} is not available")
    return event

def get_all(db: Session):
    event = db.query(model.Event).all()
    print(event)

    return event

def get_by_name(event_name: str, db: Session):
    event = db.query(model.Event).filter(
        model.Event.event_name == event_name).first()
    return event


def get_event_url(event_name: str, db: Session):
    event = db.query(model.Event).filter(
        model.Event.event_name == event_name).first()
    return event

# def get_event_url(event_name_id: str,  db: Session):
#     if  event_name_id:
#         event = db.query(model.Event).filter(
#             model.Event.id == event_name_id).first()
#     else:
#          event = db.query(model.Event).filter(
#             model.Event.event_name == event_name_id).first()
#     return event


#Event start and end date validation
def start_event(id: int, db: Session):
    time = (datetime.now().time())
    end_time = time.strftime("%H:%M:%S")
    print(end_time)
    

    attendance = db.query(model.Attendance).filter( 
        model.Attendance.participantId == id).order_by(desc(model.Attendance.attend_date)).first()
    if  attendance.time_in is None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"  user with  attendance id {id}  can not be found!")
    else: 
        attendance.time_out = time_out
    db.commit()
    db.refresh(attendance)
    return attendance
                        