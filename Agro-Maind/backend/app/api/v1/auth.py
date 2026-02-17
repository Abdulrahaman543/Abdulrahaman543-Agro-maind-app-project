from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.index import UserCreate, UserOut
from app.core.security import create_access_token
from app.services.validation_service import validate_age, validate_identification_number
from app.database import get_db

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserInDB(UserOut):
    hashed_password: str

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if not validate_age(user.age):
        raise HTTPException(status_code=400, detail="Invalid age")
    if not validate_identification_number(user.identification_number):
        raise HTTPException(status_code=400, detail="Invalid identification number")
    
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, age=user.age, identification_number=user.identification_number, hashed_password=hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.post("/login", response_model=str)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = create_access_token(data={"sub": db_user.email})
    return access_token