from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from app.utils.dbConn import Base

from sqlalchemy.orm import relationship
import datetime
from datetime import datetime


class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    gender = Column(String)
    email = Column(String, unique=True, index=True)
    organization = Column(String)
    status = Column(Boolean, default=False, index=False)
    attend_by = Column(String)
    registration_time = Column(String)
    location = Column(String)

    #attendance_id = Column(Integer, ForeignKey('attendances.id'))

    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Event", back_populates="participants")


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, unique=True)
    venue = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    number_of_participants = Column(Integer)
    description = Column(String)
    admin_id = Column(Integer, ForeignKey("admins.id"))
    participants = relationship("Participant", back_populates="event")


class Attendance(Base):
    __tablename__ = 'attendances'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    admin_id = Column(Integer, ForeignKey("admins.id"))
    participantId = Column(Integer, ForeignKey("participants.id"))
   # participants = relationship("Participant", back_populates="event")


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, index=True)
    admin_name = Column(String, unique=True)
    contact = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    event = relationship("Event")
    attendance = relationship("Attendance")
