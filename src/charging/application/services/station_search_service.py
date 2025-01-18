import pandas as pd
from datetime import datetime

from src.charging.domain.search.value_objects.postal_code import PostalCode, InvalidPostalCodeException
from src.charging.infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository
from src.charging.domain.search.events.station_search_performed import StationSearchPerformed

class ChargingStationSearchService:
    def __init__(self, repository: ChargingStationSearchRepository):
        self.repository = repository

    def search_by_postal_code(self, postal_code: str):
        validated_code = PostalCode(postal_code)
        stations = self.repository.find_by_postal_code(validated_code)
        return stations
    
    def search_by_postal_code_2(self, postal_code: str):
        validated_code = PostalCode(postal_code)
        stations = self.repository.find_by_postal_code_2(validated_code)
        locations_df = self.create_location_df(stations)
        event = StationSearchPerformed(postal_code,datetime.now(),len(stations))
        return stations, event, locations_df

    def create_location_df(self, stations):
        latitude = []
        longitude = []
        for station in stations:
            latitude.append(station.latitude)
            longitude.append(station.longitude)

        location_dict = {'latitude':latitude, 'longitude':longitude}
        location_df = pd.DataFrame(location_dict)
        
        return location_df