
#currentWorkingDirectory = "/home/ldrich/berlingeoheatmap_project1/"
#currentWorkingDirectory = "/mount/src/berlingeoheatmap1/"

# -----------------------------------------------------------------------------
#import os
#os.chdir(currentWorkingDirectory)
#print("Current working directory\n" + os.getcwd())

import pandas                           as pd
import streamlit                        as st
from src.shared import methods          as m1
from src.shared import HelperTools      as ht
from src.charging                       import search_app


from src.shared.config                  import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz   = pd.read_csv('src/shared/infrastructure/datasets/geodata_berlin_plz.csv', delimiter = ';')
    
    df_lstat        = pd.read_csv('src/shared/infrastructure/datasets/charging_stations_updated.csv')
    df_lstat2       = m1.preprop_lstat(df_lstat, df_geodat_plz, pdict)
    gdf_lstat3      = m1.count_plz_occurrences(df_lstat2)
    
    df_residents    = pd.read_csv('src/shared/infrastructure/datasets/plz_einwohner.csv')
    gdf_residents2  = m1.preprop_resid(df_residents, df_geodat_plz, pdict)

    st.title("My Streamlit App")

    layer_selection = st.radio("Select Layer", ("Station_Heat_Map", 'Station_Search'))


    if (layer_selection == 'Station_Search'):
        try:
            search_app.create_streamlit_search_interface()

        except Exception:
            st.write("The postal code you entered is invalid. Please try again.")

    if(layer_selection == 'Station_Heat_Map'):
        m1.make_streamlit_electric_Charging_resid(gdf_lstat3, gdf_residents2)
# -----------------------------------------------------------------------------------------------------------------------

    #


if __name__ == "__main__": 
    main()

