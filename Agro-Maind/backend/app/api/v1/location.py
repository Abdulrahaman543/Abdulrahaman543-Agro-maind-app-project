from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import geopy.distance

router = APIRouter()

class LocationRequest(BaseModel):
    latitude: float
    longitude: float

class LocationResponse(BaseModel):
    is_within_area: bool
    message: str

# Define the geographical area (example coordinates)
AREA_COORDINATES = [(12.9715987, 77.594566), (12.2958104, 76.6393805)]  # Example coordinates for a rectangular area

@router.post("/check-location", response_model=LocationResponse)
async def check_location(location: LocationRequest):
    user_location = (location.latitude, location.longitude)
    
    # Check if the user's location is within the defined area
    for area in AREA_COORDINATES:
        if geopy.distance.distance(user_location, area).km < 5:  # 5 km radius check
            return LocationResponse(is_within_area=True, message="You are within the allowed area.")
    
    raise HTTPException(status_code=403, detail="You are outside the allowed area.")