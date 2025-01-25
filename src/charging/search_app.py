import streamlit as st
import folium
from streamlit_folium import folium_static
from src.charging.infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository
from src.charging.application.services.station_search_service import ChargingStationSearchService
from src.charging.domain.search.value_objects.postal_code import InvalidPostalCodeException


def create_streamlit_search_interface():

    user_input = (st.text_input("Enter a Postal Code:"))

    if user_input:
        try:
            repository = ChargingStationSearchRepository()
            service = ChargingStationSearchService(repository)
            
            stations, event = service.search_by_postal_code_2(user_input)
            if(len(stations) == 0):
                st.write('There are no charging stations in this postal code. Please try again.')
            else:
                #instantiate map
                map = folium.Map([stations[0].latitude,stations[0].longitude], zoom_start=15)
                
                #add markers for each station
                locations =[]
                for station in stations:
                    location = station.get_station_location()
                    availability = 'Available' if station.check_availability() else 'Not Available'
                    message = f'Station ID: {station.get_id()}\nThis station is '+availability
                    folium.Marker(location, popup=folium.Popup(message, max_width = 100)).add_to(map)
                    locations.append(location)

                #display map
                map.fit_bounds(locations)
                folium_static(map, width=700, height=500)

        except InvalidPostalCodeException:
            st.write("The postal code you entered is invalid. Please try again.")

    return