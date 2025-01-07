import pandas as pd
from domain.search.value_objects.postal_code import PostalCode

class ChargingStationSearchRepository:
    def __init__(self):
        self._stations = []

    def find_by_postal_code(self, postal_code: PostalCode):
        """Find charging stations that match the given postal code."""
        df = pd.read_csv('charging/infrastructure/datasets/charging_stations_updated.csv')

        postal_code_int = int(postal_code.value)
        
        # Filter the DataFrame for rows matching the postal code
        filtered_rows = df[df['Postleitzahl'] == postal_code_int]
        return filtered_rows
        
