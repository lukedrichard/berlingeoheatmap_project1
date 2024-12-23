# Documentation

## Program Structure

### Core Files
- **`main.py`**:
  - Central script to run the Streamlit app.
  - Uses methods from `core/methods.py` to process and visualize data.
- **`core/methods.py`**:
  - Contains reusable functions for tasks like loading data, processing population-to-charging-station ratios, and geospatial plotting.
- **`config.py`**:
  - Stores configuration details, such as file paths and relevant column names.

### Data Sources
1. **Charging Stations Data** (`charging_stations_updated.csv`):
   - Cleaned version of the original `Ladesaeulenregister.csv` dataset with the heading removed manually.
   - Contains metadata and geographic locations of electric charging stations in Berlin.
2. **Population Data** (`plz_einwohner.csv`):
   - Includes population statistics mapped by postal codes in Berlin.
3. **Geospatial Data** (`geodata_berlin_plz.csv`):
   - Provides geospatial information for mapping Berlin's postal code districts.

### Workflow
1. **Data Import**:
   - Load charging station, population, and geospatial data into the program.
2. **Data Processing**:
   - Merge datasets using postal codes as the key.
   - Compute critical metrics like the population-to-charging-station ratio.
3. **Geospatial Analysis**:
   - Map these metrics to postal code regions within Berlin using geospatial data.
4. **Visualization**:
   - Use Streamlit to create an interactive heatmap showcasing the analysis.

### Streamlit Integration
- The app visualizes the relationship between population density and charging station availability interactively.
- Users can identify high-demand zones directly on the map.

---

## Interpretation of Results

### High-Demand Areas
- Postal codes with:
  - High population density.
  - A low number of charging stations relative to the population.
- Example: Inner-city neighborhoods where private charging infrastructure is limited.

### Low-Demand Areas
- Postal codes with:
  - Lower population density.
  - Sufficient charging stations, typically in suburban regions with access to private chargers.

### Recommendations
1. **Focus on Inner-city Districts**:
   - These areas should be prioritized for installing additional charging stations.
2. **Improve Dataset Accuracy**:
   - Adding housing type data and vehicle ownership rates can enhance the demand model.
3. **Dynamic Updates**:
   - Integrating real-time data can help monitor charging station usage and demand patterns.

### Potential Improvements
- Include housing type ratios to refine demand calculations.
- Incorporate real-time updates to visualize charging station usage dynamically.
- Allow users to submit feedback on charging station demand via the app.
