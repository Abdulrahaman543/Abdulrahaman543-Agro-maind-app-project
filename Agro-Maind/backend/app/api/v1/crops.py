from fastapi import APIRouter, HTTPException
from typing import List
from ..models.crop import Crop
from ..schemas.index import CropSchema

router = APIRouter()

# Sample data for crops
crops_data = [
    {"id": 1, "name": "Wheat", "growth_conditions": "Temperate climate, well-drained soil"},
    {"id": 2, "name": "Rice", "growth_conditions": "Warm climate, flooded fields"},
    {"id": 3, "name": "Corn", "growth_conditions": "Warm climate, fertile soil"},
]

@router.get("/crops", response_model=List[CropSchema])
async def get_crops():
    return crops_data

@router.get("/crops/{crop_id}", response_model=CropSchema)
async def get_crop(crop_id: int):
    crop = next((crop for crop in crops_data if crop["id"] == crop_id), None)
    if crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    return crop

@router.post("/crops", response_model=CropSchema)
async def create_crop(crop: CropSchema):
    new_crop = crop.dict()
    new_crop["id"] = len(crops_data) + 1
    crops_data.append(new_crop)
    return new_crop

@router.put("/crops/{crop_id}", response_model=CropSchema)
async def update_crop(crop_id: int, crop: CropSchema):
    existing_crop = next((c for c in crops_data if c["id"] == crop_id), None)
    if existing_crop is None:
        raise HTTPException(status_code=404, detail="Crop not found")
    existing_crop.update(crop.dict())
    return existing_crop

@router.delete("/crops/{crop_id}", response_model=dict)
async def delete_crop(crop_id: int):
    global crops_data
    crops_data = [crop for crop in crops_data if crop["id"] != crop_id]
    return {"message": "Crop deleted successfully"}