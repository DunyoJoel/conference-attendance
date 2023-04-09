from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.security.hashing import Hash
from app.models import model
from app.utils import schemas


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
                                            registry_from=request.registry_from
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
    participant.registry_from = request.registry_from

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
        # participants = db.query(model.Participant).filter(
        #     model.Participant.attend_by == "onsite").order_by(
        #     model.Participant.attend_by).all()
        # participant = participants[0] if participants else None
    return participant


# s
# def get_all_by_event(id: int, db: Session):
#     participants = db.query(model.Event).filter(
#         model.Event.id == id).outerjoin(
#         model.Participant).all()
#     print(participants)

#     return participants

# def get_participants_by_event(db: Session, event_name: str):
#     participants = db.query(model.Participant).filter(
#         model.Participant.event_id == event_name).outerjoin(
   #     model.Event).all()
#     return participants

def get_all_by_event(id: int, db: Session):
    event = db.query(model.Event).filter(model.Event.id == id).first()
    participants = event.participants
    print(participants)

    return participants