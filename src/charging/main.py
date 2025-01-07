# Now import your modules
from infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository
from application.services.station_search_service import ChargingStationSearchService

# Initialize repository and service
repository = ChargingStationSearchRepository()
service = ChargingStationSearchService(repository)

# Perform a search
postal_code_to_search = "72537"  # Example Berlin postal code
stations = service.search_by_postal_code(postal_code_to_search)

if len(stations) > 0:
    print(f"{len(stations)} Charging stations in postal code {postal_code_to_search}:")
else:
    print("No charging stations found for the given postal code.")
