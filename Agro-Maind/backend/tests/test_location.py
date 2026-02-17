import pytest
from app.api.v1.location import validate_location
from fastapi import HTTPException

def test_validate_location_valid():
    # Test with a valid location
    location_data = {"latitude": 12.9716, "longitude": 77.5946}  # Example coordinates for Bangalore
    result = validate_location(location_data)
    assert result is True

def test_validate_location_invalid():
    # Test with an invalid location
    location_data = {"latitude": 100.0, "longitude": 200.0}  # Out of bounds coordinates
    with pytest.raises(HTTPException) as exc_info:
        validate_location(location_data)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid location coordinates."

def test_validate_location_missing_data():
    # Test with missing location data
    location_data = {"latitude": 12.9716}  # Missing longitude
    with pytest.raises(HTTPException) as exc_info:
        validate_location(location_data)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Location data must include both latitude and longitude."