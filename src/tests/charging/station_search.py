from src.charging.application.services.station_search_service import ChargingStationSearchService
from src.charging.domain.search.events.station_search_performed import StationSearchPerformed
from src.charging.domain.search.value_objects.postal_code import InvalidPostalCodeException
from src.charging.infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository
import pytest

def test_search_stations_by_valid_postal_code():
    #edge case 1: 10115
    postal_code = "10115"
    service = ChargingStationSearchService(ChargingStationSearchRepository())

    stations, event  = service.search_by_postal_code_2(postal_code)
    
    assert isinstance(event, StationSearchPerformed)
    assert len(stations) > 1
    assert all(station.is_in_postal_code(postal_code)
               for station in stations)
    
    #edge case 2: 14199
    stations, event  = service.search_by_postal_code_2(postal_code)
    
    assert isinstance(event, StationSearchPerformed)
    assert len(stations) > 1
    assert all(station.is_in_postal_code(postal_code)
               for station in stations)
    
def test_invalid_berlin_postal_code():
    service = ChargingStationSearchService(ChargingStationSearchRepository())

    #prefix not 10,12,13,14
    with pytest.raises(InvalidPostalCodeException):
        service.search_by_postal_code_2("20159")
    #too short/long
    with pytest.raises(InvalidPostalCodeException):
        service.search_by_postal_code_2('1234')

    with pytest.raises(InvalidPostalCodeException):
        service.search_by_postal_code_2('101150')

    #alphanumeric
    with pytest.raises(InvalidPostalCodeException):
        service.search_by_postal_code_2('a')
    
    with pytest.raises(InvalidPostalCodeException):
        service.search_by_postal_code_2('12a')

    #empty/missing
    with pytest.raises(InvalidPostalCodeException):
        service.search_by_postal_code_2('')
    