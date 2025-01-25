import pandas as pd
from src.charging.domain.search.value_objects.postal_code import PostalCode
from src.charging.domain.search.entities.charging_station import ChargingStation

class ChargingStationSearchRepository:
    def __init__(self):
        self._stations = []
        self.fill_from_csv('src/charging/infrastructure/datasets/charging_stations_updated.csv')

    def find_by_postal_code(self, postal_code: PostalCode):
        """Uses csv file to find charging stations that match the given postal code."""
        df = pd.read_csv('infrastructure/datasets/charging_stations_updated.csv')

        postal_code_int = int(postal_code.value)
        
        # Filter the DataFrame for rows matching the postal code
        filtered_rows = df[df['Postleitzahl'] == postal_code_int]
        return filtered_rows

    def find_by_postal_code_2(self, postal_code: PostalCode):
        """Uses self.stations to find the stations which match the given postal code"""
        stations_in_postal_code = []
        for station in self._stations:
            if station.is_in_postal_code(postal_code.value):
                stations_in_postal_code.append(station)

        return stations_in_postal_code
    
    def add_charging_station(self, new_station :ChargingStation):
        self._stations.append(new_station)
        return
    
    def remove_chargin_station():
        return
    
    def fill_from_csv(self, path_to_csv: str):
    
        df = pd.read_csv(path_to_csv)
        for index, row in df.iterrows():
            id = str(index)
            postal_code = str(row['Postleitzahl'])
            latitude = float(str(row['Breitengrad']).replace(',', '.'))
            longitude = float(str(row['Längengrad']).replace(',','.'))
           
            self.add_charging_station(ChargingStation(id, postal_code, latitude, longitude))

        return
    