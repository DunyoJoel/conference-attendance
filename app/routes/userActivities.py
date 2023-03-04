from fastapi import APIRouter, Depends, Security, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.utils import schemas, dbConn
from app.security import token
from app.repo import participants, events, attendances,admins

from app.utils.initialUser import User
from app.security import oauth2
from typing import List

router = APIRouter()
get_db = dbConn.get_db


# route for department
@router.post('/event/add', response_model=schemas.ShowEvent, tags=['Admin', ])
async def create_event(request: schemas.CreateEvent,
                       db: Session = Depends(get_db),
                       current_user: schemas.ShowAdmin = Security(
                           oauth2.get_current_active_user

                       )):
    return events.create(request, db, current_user)


@router.delete('/event/{id}',  response_model=schemas.ShowEvent, tags=['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return events.destroy(id, db)


@router.put('/event/update',  response_model=schemas.ShowEvent, tags=['Admin'])
async def update(request: schemas.UpdateEvent, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return events.update(request.id, request, db)


@router.get('/event/{id}',  response_model=schemas.ShowEvent, tags=['Admin'])
async def show_event(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return events.show(id, db)


@router.get('/event/', response_model=List[schemas.EventWithAdmin], tags=['Admin'])
async def show_event_all(db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return events.get_all(db)



# route for user
@router.post('/participant/add', response_model=schemas.ShowParticipant, tags=['Admin', ])
async def create_participant(request: schemas.CreateParticipant,
                             db: Session = Depends(get_db),
                             current_user: schemas.ShowAdmin = Security(
                                 oauth2.get_current_active_user

                             )):
    return participants.create(request, db, current_user)


@router.get('/participant/{id}',  response_model=schemas.ShowParticipant, tags=['Admin'])
async def show_participant(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return participants.show(id, db)


@router.get('/participant/', response_model=List[schemas.ParticipantWithAdmin], tags=['Admin'])
async def show_participant_all(db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return participants.get_all(db)


@router.put('/participant/update',  response_model=schemas.ShowParticipant, tags=['Admin'])
async def update(request: schemas.UpdateParticipant, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return participants.update(request.id, request, db)


@router.delete('/participant/{id}', response_model=schemas.ShowParticipant, tags=['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return participants.destroy(id, db)


# route for admin
@router.post('/admin/add', response_model=schemas.ShowAdmin, tags=['Admin', ])
async def create_admin(request: schemas.CreateAdmin,
                       db: Session = Depends(get_db),
                       current_user: schemas.ShowAdmin = Security(
                           oauth2.get_current_active_user

                       )):
    return admins.create_new_admin(request, db, current_user)


@router.get('/admin/{id}',  response_model=schemas.ShowAdmin, tags=['Admin'])
async def show_admin(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return admins.show(id, db)


@router.put('/admin/update',  response_model=schemas.ShowAdmin, tags=['Admin'])
async def update(request: schemas.UpdateAdmin, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return admins.update(request.id, request, db)


@router.delete('/admin/{id}', response_model=schemas.ShowAdmin, tags=['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return admins.destroy(id, db)


# route for attendance
@router.get('/attendance/{id}',  response_model=schemas.ShowAttendance, tags=['Admin'])
async def show_attendance(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return attendances.showAttendance(id, db)


@router.delete('/attendance/{id}', response_model=schemas.ShowAttendance, tags=['Admin'])
async def destroy(id: int, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return attendances.destroy(id, db)


@router.get('/attendance/', response_model=List[schemas.ShowAttendance], tags=['Admin'])
async def show_attendance_all(db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return attendances.get_all(db)


@router.put('/attendance/update',  response_model=schemas.ShowAttendance, tags=['Admin'])
async def update(request: schemas.UpdateAttendance, db: Session = Depends(get_db),  current_user: schemas.ShowAdmin = Security(
        oauth2.get_current_active_user,

)):
    return attendances.update(request.id, request, db)


# @router.post('/attendance/user_login', response_model=schemas.ShowUser, tags=['User', ])
# async def user_login(phone_number: str,
#                      db: Session = Depends(get_db)
#                      ):
#     return users.userByphoneNumber(phone_number, db)


# @router.post('/attendance/user_attendance_login', response_model=schemas.ShowAttendance, tags=['User', ])
# async def user_attendance_login(id: int,
#                                 db: Session = Depends(get_db)
#                                 ):
#     return attendances.login_attendance(id, db)


# @router.post('/attendance/user_attendance_logout', response_model=schemas.ShowAttendance, tags=['User', ])
# async def user_attendance_logout(id: int,
#                                  db: Session = Depends(get_db)
#                                  ):
#     return attendances.logout_attendance(id, db)
