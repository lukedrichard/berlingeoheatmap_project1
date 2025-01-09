from dataclasses import dataclass
from src.charging.domain.search.value_objects.postal_code import PostalCode

@dataclass
class ChargingStation:
    postal_code: str
    latitude: float
    longitude: float
    available: bool = True

    
    def is_in_postal_code(self, code: str) -> bool:
        return self.postal_code == code
