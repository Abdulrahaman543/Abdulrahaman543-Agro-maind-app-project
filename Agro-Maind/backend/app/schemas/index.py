from pydantic import BaseModel
from typing import List, Optional

class UserSchema(BaseModel):
    username: str
    age: int
    country: str
    identification_number: str

class CropSchema(BaseModel):
    crop_type: str
    growth_conditions: str
    expected_yield: Optional[float] = None

class UserResponseSchema(BaseModel):
    user: UserSchema
    message: str

class CropResponseSchema(BaseModel):
    crop: CropSchema
    message: str

class ErrorResponseSchema(BaseModel):
    error: str
    details: Optional[str] = None

class LocationSchema(BaseModel):
    latitude: float
    longitude: float
    user_id: str

class LocationResponseSchema(BaseModel):
    location: LocationSchema
    message: str