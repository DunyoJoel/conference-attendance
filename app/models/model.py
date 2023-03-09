from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from app.utils.dbConn import Base

from sqlalchemy.orm import relationship

from datetime import datetime


class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    gender = Column(String)
    email = Column(String, unique=True, index=True)
    organization = Column(String)
    registry_from = Column(String)
    #attendance_id = Column(Integer, ForeignKey('attendances.id'))

    event = relationship('Event', back_populates='participants')


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, unique=True)
    venue = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    number_of_participants = Column(Integer)
    description = Column(String)
    admin_id = Column(Integer, ForeignKey("admins.id"))
    participantId = Column(Integer, ForeignKey("participants.id"))
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
