import streamlit as st
import folium
from streamlit_folium import st_folium
from src.charging.infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository
from src.charging.application.services.station_search_service import ChargingStationSearchService


def create_streamlit_search_interface():

    user_input = (st.text_input("Enter a Postal Code:"))

    try:
        repository = ChargingStationSearchRepository()
        #repository.fill_from_csv('src/charging/infrastructure/datasets/charging_stations_updated.csv')
        service = ChargingStationSearchService(repository)
        
        stations, event, locations_df = service.search_by_postal_code_2(user_input)
        if(len(stations) == 0):
            st.write('There are no charging stations in this postal code. Please try again.')
        else:
            #st.map(locations_df, color = '#0000FF', size = 15)
            #instantiate map
            map = folium.Map([stations[0].latitude,stations[0].longitude], zoom_start=15)
            #add markers for each station
            
            locations =[]
            for station in stations:
                location = [station.latitude, station.longitude]
                availability = 'Available' if station.available else 'Not Available'
                message = f'Station ID: {station.id}\nThis station is '+availability
                folium.Marker(location, popup=folium.Popup(message, max_width = 100)).add_to(map)
                locations.append(location)
            #display the map
            map.fit_bounds(locations)
            st_data = st_folium(map, width=700, height=500)

    except Exception:
        st.write("The postal code you entered is invalid. Please try again.")

    return
