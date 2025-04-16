import dask.dataframe as dd
import folium
from folium.plugins import MarkerCluster

# Chemin vers le fichier CSV volumineux
file_path = 'cell_towers_processed.csv'

# Charger le fichier CSV avec Dask
ddf = dd.read_csv(file_path)

# Filtrer les données pour une région spécifique
latitude_range = (43.0, 50.0)  # Exemple pour la France métropolitaine
longitude_range = (-1.5, 7.5)

# Filtrer les données avec Dask
filtered_ddf = ddf[(ddf['lat'] >= latitude_range[0]) & (ddf['lat'] <= latitude_range[1]) & 
                   (ddf['lon'] >= longitude_range[0]) & (ddf['mcc'] == 208)]

# Convertir le DataFrame Dask filtré en DataFrame Pandas
filtered_df = filtered_ddf.compute()

# Initialiser la carte Folium
map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Initialiser le cluster de marqueurs
marker_cluster = MarkerCluster().add_to(map)

# Ajouter des marqueurs pour chaque tour cellulaire
for index, row in filtered_df.iterrows():
    lat = row['lat']
    lon = row['lon']
    mcc = row['mcc']
    mnc = row['net']
    lac = row['area']
    cell_id = row['cell']
    popup_text = f"MCC: {mcc}<br>MNC: {mnc}<br>LAC: {lac}<br>Cell ID: {cell_id}"
    folium.Marker(location=[lat, lon], popup=popup_text).add_to(marker_cluster)
    
# Sauvegarder la carte dans un fichier HTML
map.save('cell_towers_map.html')

print("Carte de tours cellulaires créée : cell_towers_map.html")
