import pandas as pd

stations_df = pd.read_csv('charging_stations_updated.csv')
print(stations_df.columns)

population_df = pd.read_csv('plz_einwohner.csv')
print(population_df)

geo_df = pd.read_csv('datasets/geodata_berlin_plz.csv', delimiter = ';')
print(geo_df)