from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class MalfunctionReport:
    postal_code: str
    station_id: str
    user_name: str
    user_email: str
    user_phone_number: str
    description: str
    timestamp: datetime
    resolved: bool = False
