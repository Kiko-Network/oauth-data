from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    token: str

class AirQualityDataResponse(BaseModel):
    id: int
    device_id: int
    pm2_5: float
    pm1_0: float
    pm10: float
    temperature: float
    humidity: float
    timestamp_epoch: int
    timestamp_utc: datetime

    class Config:
        orm_mode = True

