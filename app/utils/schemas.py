from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class CreateParticipant(BaseModel):
    # id: int
    name: str
    gender: str
    phone_number: str
    email: str
    organization: str
    registry_from: str

    class Config():
        orm_mode = True


class ShowParticipant(BaseModel):
    id: int
    name: str
    gender: str
    phone_number: str
    email: str
    organization: str
    registry_from: str

    class Config():
        orm_mode = True


class ShowParticipantPhone(BaseModel):
    # id: int
    name: str
    gender: str
    phone_number: str
    email: str
    organization: str
    registry_from: str

    class Config():
        orm_mode = True


class UpdateParticipant(BaseModel):
    id: int
    name: str
    gender: str
    phone_number: str
    email: str
    organization: str
    registry_from: str

    class Config():
        orm_mode = True


# class CreateAttendance(BaseModel):
#     status: str
#     participantId: str = None
#     admin_id: str = None

#     class Config():
#         orm_mode = True


class ShowAttendance(BaseModel):
    id: int
    participantId: int

    class Config():
        orm_mode = True


class CreateEvent(BaseModel):
    event_name: str
    venue: str
    start_date: datetime
    end_date: datetime
    number_of_participants: int
    description: str

    class Config():
        orm_mode = True


class CreateEventUrl(BaseModel):
    id: int
    event_name: str
    description: str

    class Config():
        orm_mode = True


class ShowEvent(BaseModel):
    id: int
    event_name: str
    admin_id: int
    venue: str
    start_date: datetime
    end_date: datetime
    number_of_participants: int
    description: str

    class Config():
        orm_mode = True


class ShowEventAll(BaseModel):
    id: int
    event_name: str
    venue: str
    start_date: datetime
    end_date: datetime
    number_of_participants: int
    description: str

    class Config():
        orm_mode = True


class UpdateEvent(BaseModel):
    id: int
    event_name: str
    venue: str
    start_date: datetime
    end_date: datetime
    number_of_participants: int
    description: str

    class Config():
        orm_mode = True


class UpdateAttendance(BaseModel):
    id: int
    status: str

    class Config():
        orm_mode = True


class CreateAdmin(BaseModel):
    email: str
    admin_name: str
    contact: str
    password: str

    class Config():
        orm_mode = True


class ShowAdmin(BaseModel):
    id: int
    email: str

    class Config():
        orm_mode = True


class UpdateAdmin(BaseModel):
    id: int
    email: str
    password: str

    class Config():
        orm_mode = True


class TokenPayload(BaseModel):
    email: str = None
    contact: str = None
    exp: int = None


class EventWithAdmin(BaseModel):
    Department: ShowEvent = None
    Admin: ShowAdmin = None

    class Config():
        orm_mode = True


class ParticipantWithAdmin(BaseModel):
    User: ShowParticipant = None
    Admin: ShowAdmin = None
