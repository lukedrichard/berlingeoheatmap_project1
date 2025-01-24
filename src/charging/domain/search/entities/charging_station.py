from dataclasses import dataclass
from src.charging.domain.search.value_objects.postal_code import PostalCode

@dataclass
class ChargingStation:
    id: str
    postal_code: str
    latitude: float
    longitude: float
    available: bool = True

    
    def is_in_postal_code(self, code: str) -> bool:
        return self.postal_code == code
    
    def get_station_location(self):
        return [self.latitude, self.longitude]

    def check_availability(self) -> bool:
        return self.available
    
    def get_id(self) -> str:
        return self.id