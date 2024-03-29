from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model
from app.utils import schemas
from datetime import datetime


def create(request: schemas.CreateParticipant, db: Session):
    participant = db.query(model.Participant).filter(
        model.Participant.name == request.name).first()
    if participant:
        raise HTTPException(status_code=303,
                            detail=f"User with the name { request.name} already exist")
    else:
        new_participant = model.Participant(name=request.name,
                                            phone_number=request.phone_number,
                                            gender=request.gender,
                                            email=request.email,
                                            organization=request.organization,
                                            status=request.status,
                                            attend_by=request.attend_by,
                                            registration_time=request.registration_time,
                                            location=request.location,
                                            event_id=request.event_id
                                            )

        db.add(new_participant)
        db.commit()
        db.refresh(new_participant)
        return new_participant


def show(id: int, db: Session):
    participant = db.query(model.Participant).filter(
        model.Participant.id == id).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"participant with the id {id} is not available")
    return participant


def participantByphoneNumber(phone_number: str, db: Session):
    participant = db.query(model.Participant).filter(
        model.Participant.phone_number == phone_number).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the phone number  {phone_number} is not available")
    return participant
# def showLoginUser(current_user, db: Session):
#     loginUser =db.query(model.User, model.Sensor).outerjoin(model.Sensor).filter(model.User.id == current_user.id).first()
#     if not loginUser:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return loginUser


def get_all(db: Session):
    participant = db.query(model.Participant).all()
    print(participant)

    return participant

# def get_all_admin(db: Session):
#     admin = db.query(model.User).filter(model.User.action_by is not None).all()
#     return admin


def destroy(id: int, db: Session):
    participant = db.query(model.Participant).filter(
        model.Participant.id == id).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"participant with id {id} not found")
    db.delete(participant)
    db.commit()
    return participant


def update(id: int, request: schemas.ShowParticipant, db: Session):
    participant = db.query(model.Participant).filter(
        model.Participant.id == id).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"participant with id {id} not found")

    participant.name = request.name
    participant.phone_number = request.phone_number
    participant.gender = request.gender
    participant.email = request.email
    participant.organization = request.organization
    participant.status = request.status
    participant.attend_by = request.attend_by
    participant.registration_time = request.registration_time
    participant.location = request.location
    participant.event_id = request.event_id

    db.commit()
    db.refresh(participant)
    return participant


def showParticipant(db: Session, name: str):
    participant = db.query(model.Participant).filter(
        model.Participant.name == name).first()
    if not participant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {name} is not available")
    return participant


def get_by_name(phone_number: str, db: Session):
    participant = db.query(model.Participant).filter(
        model.Participant.phone_number == phone_number).first()
    return participant


def get_by_phone_number(phone_number_email: str,  db: Session):
    if "@" in phone_number_email:
        participant = db.query(model.Participant).filter(
            model.Participant.email == phone_number_email).first()
    else:
        participant = db.query(model.Participant).filter(
            model.Participant.phone_number == phone_number_email).first()
    return participant


def attend_event_by(attend_by: str, db: Session) -> model.Participant:
    if attend_by == "virtual":
        participant = db.query(model.Participant).filter(
            model.Participant.attend_by == "virtual").all()

    else:
        participant = db.query(model.Participant).filter(
            model.Participant.attend_by == "onsite").all()

    return participant
# status of registrations
def participant_event_status(participant_id: int, registration_time: str, db: Session) -> model.Participant:
    event_start_date = db.query(model.Event).first().start_date
    existing_participant = db.query(model.Participant).filter(model.Participant.id == participant_id).first()
    if existing_participant:
        if registration_time >= event_start_date and not existing_participant.status:
            existing_participant.status = True
    else:
        new_participant = model.Participant(id=participant_id, registration_time=registration_time, status=True)
        db.add(new_participant)
        db.flush()
        existing_participant = new_participant

    return existing_participant

# def participant_event_status(participant_id: int, status: int, db: Session):
#     participant = db.query(model.Participant).filter(
#         model.Participant.id == participant_id).first()
#     if not participant:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"participant with id {participant_id} not found")

#     event = db.query(model.Event).filter(
#         model.Event.id == participant.event_id).first()
#     if not event:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"event with id {participant.event_id} not found")

#     participant.status = status
#     event.start_date = datetime.now()

#     db.commit()
#     db.refresh(participant)
#     db.refresh(event)

#     return participant


def get_all_by_event(id: int, db: Session):
    participant = db.query(model.Participant).filter(
        model.Participant.event_id == model.Event.id).filter(model.Event.id == id).all()

    print(participant)

    return participant
