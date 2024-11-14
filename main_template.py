
currentWorkingDirectory = "/home/ldrich/berlingeoheatmap_project1/"
#currentWorkingDirectory = "/mount/src/berlingeoheatmap1/"

# -----------------------------------------------------------------------------
import os
os.chdir(currentWorkingDirectory)
print("Current working directory\n" + os.getcwd())

import pandas                        as pd
from core import methods             as m1
from core import HelperTools         as ht

from config                          import pdict

# -----------------------------------------------------------------------------
@ht.timer
def main():
    """Main: Generation of Streamlit App for visualizing electric charging stations & residents in Berlin"""

    df_geodat_plz   = pd.read_csv('plz_einwohner.csv')
    
    df_lstat        = pd.read_csv('Ladesaeulenregister.csv', delimiter = ';')
    #df_lstat2       = #
    #gdf_lstat3      = #
    
    #df_residents    = #
    #gdf_residents2  = #
    
# -----------------------------------------------------------------------------------------------------------------------

    #


if __name__ == "__main__": 
    main()

