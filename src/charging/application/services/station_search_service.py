import pandas as pd
import streamlit as st

from src.charging.domain.search.value_objects.postal_code import PostalCode
from src.charging.infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository

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
        self.create_location_df(stations)
        return

    def create_location_df(self, stations):
        latitude = []
        longitude = []
        for station in stations:
            latitude.append(station.latitude)
            longitude.append(station.longitude)

        location_dict = {'latitude':latitude, 'longitude':longitude}
        location_df = pd.DataFrame(location_dict)
        st.map(location_df, color = '#0000FF', size = 15)
        return