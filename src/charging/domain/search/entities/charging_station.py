from dataclasses import dataclass
from domain.search.value_objects.postal_code import PostalCode

@dataclass
class ChargingStation:
    postal_code: PostalCode
    latitude: str
    Longitude: str
    available: bool = True

    def is_in_postal_code(self, code: str) -> bool:
        return self.postal_code == code
