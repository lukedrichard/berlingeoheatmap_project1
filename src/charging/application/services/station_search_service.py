from domain.search.value_objects.postal_code import PostalCode
from infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository

class ChargingStationSearchService:
    def __init__(self, repository: ChargingStationSearchRepository):
        self.repository = repository

    def search_by_postal_code(self, postal_code: str):
        validated_code = PostalCode(postal_code)
        stations = self.repository.find_by_postal_code(validated_code)
        return stations
