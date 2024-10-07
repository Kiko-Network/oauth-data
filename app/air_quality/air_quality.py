# File: air_quality.py
from fastapi import APIRouter, Depends, HTTPException, status, Header, Request
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from datetime import datetime
from typing import List, Optional

router = APIRouter()

def get_user_by_token(token: str, db: Session):
    db_token = db.query(models.Token).filter(models.Token.token == token).first()
    if not db_token:
        return None
    return db.query(models.User).filter(models.User.id == db_token.user_id).first()

def log_fetch(user_id: int, endpoint: str, db: Session):
    log = models.FetchLog(user_id=user_id, endpoint=endpoint, timestamp=datetime.utcnow())
    db.add(log)
    # Fetch the IDs of the entries you want to delete
    old_logs = db.query(models.FetchLog.id).order_by(models.FetchLog.id.desc()).offset(200).all()
    
    # Extract IDs and delete entries
    if old_logs:
        db.query(models.FetchLog).filter(models.FetchLog.id.in_([log.id for log in old_logs])).delete(synchronize_session=False)
    
    db.commit()

@router.get("/data", response_model=List[schemas.AirQualityDataResponse])
async def get_air_quality(
    request: Request,
    start: Optional[int] = None,
    end: Optional[int] = None,
    db: Session = Depends(get_db)
):
    # Access the Authorization header directly from the request object
    authorization = request.headers.get("Authorization")
    
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing")
    
    # Extract the token from the Authorization header
    token = authorization.split("Bearer ")[-1] if "Bearer " in authorization else None
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token format")
    
    user = get_user_by_token(token, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    log_fetch(user.id, "/data", db)
    
    query = db.query(models.AirQualityData)
    
    if start and end:
        query = query.filter(
            models.AirQualityData.timestamp_epoch >= start,
            models.AirQualityData.timestamp_epoch <= end
        )
        data = query.order_by(models.AirQualityData.timestamp_utc).all()
    else:
        data = query.order_by(models.AirQualityData.timestamp_utc.desc()).limit(10).all()
    
    return data
