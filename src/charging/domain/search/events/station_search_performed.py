from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class StationSearchPerformed:
    postal_code: str
    timestamp: datetime
    stations_found: int
