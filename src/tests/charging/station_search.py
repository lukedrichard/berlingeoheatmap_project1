from charging.application.services.station_search_service import ChargingStationSearchService
from charging.domain.search.events.station_search_performed import StationSearchPerformed
from charging.domain.search.value_objects.postal_code import InvalidPostalCodeException
from charging.infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository
import pytest

def test_search_stations_by_valid_postal_code():
    postal_code = "10115"
    service = ChargingStationSearchService(ChargingStationSearchRepository())

    result = service.search_by_postal_code(postal_code)

    assert isinstance(result.event, StationSearchPerformed)
    assert len(result.stations) > 1
    assert all(station.is_in_postal_code(postal_code)
                for station in result.stations)
    
def test_invalid_berlin_postal_code():
    service = ChargingStationSearchService(ChargingStationSearchRepository())

    with pytest.raises(InvalidPostalCodeException):
        service.search_by_postal_code("12345")