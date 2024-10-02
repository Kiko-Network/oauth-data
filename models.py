from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    mac_address = Column(String, unique=True, index=True)
    
class AirQualityData(Base):
    __tablename__ = "air_quality_data"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer)
    pm2_5 = Column(Float)
    pm1_0 = Column(Float)
    pm10 = Column(Float)
    temperature = Column(Float)  # New field
    humidity = Column(Float)     # New field
    timestamp_epoch = Column(Integer)
    timestamp_utc = Column(DateTime)

class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    token = Column(String, unique=True, index=True)

class FetchLog(Base):
    __tablename__ = "fetch_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    endpoint = Column(String)
    timestamp = Column(DateTime)

