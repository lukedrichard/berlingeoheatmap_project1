#currentWorkingDirectory = "/home/ldrich/berlingeoheatmap_project1/src/"
#currentWorkingDirectory = "/mount/src/berlingeoheatmap1/"

#import os
#os.chdir(currentWorkingDirectory)

# Now import your modules
import streamlit as st
from src.charging.infrastructure.repositories.charging_station_search_repository import ChargingStationSearchRepository
from src.charging.application.services.station_search_service import ChargingStationSearchService


# Initialize repository and service
#repository = ChargingStationSearchRepository()
#service = ChargingStationSearchService(repository)

# Perform a search
#postal_code_to_search = "72537"  # Example Berlin postal code
#stations = service.search_by_postal_code(postal_code_to_search)
#if len(stations) > 0:
#    print(f"{len(stations)} Charging stations in postal code {postal_code_to_search}:")
#else:
#    print("No charging stations found for the given postal code.")


def create_streamlit_search_interface():
    repository = ChargingStationSearchRepository()
    #repository.fill_from_csv('src/charging/infrastructure/datasets/charging_stations_updated.csv')
    service = ChargingStationSearchService(repository)

    user_input = (st.text_input("Enter a Postal Code:"))
    try:
        stations, locations_df = service.search_by_postal_code_2(user_input)
        if(len(stations) == 0):
            st.write('There are no charging stations in this postal code. Please try again.')
        else:
            st.map(locations_df, color = '#0000FF', size = 15)
    except Exception:
        st.write("The postal code you entered is invalid. Please try again.")

    return
