from geopy.geocoders import Nominatim
from fastapi import HTTPException

class LocationService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="agro_maind")

    def get_location(self, latitude: float, longitude: float):
        try:
            location = self.geolocator.reverse((latitude, longitude), exactly_one=True)
            return location.address if location else None
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def is_within_area(self, latitude: float, longitude: float, area_bounds: dict) -> bool:
        if (area_bounds['southwest']['lat'] <= latitude <= area_bounds['northeast']['lat'] and
                area_bounds['southwest']['lng'] <= longitude <= area_bounds['northeast']['lng']):
            return True
        return False