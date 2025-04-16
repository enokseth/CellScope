import dask.dataframe as dd
import folium
from folium.plugins import MarkerCluster

# Fonction pour obtenir les codes MCC/MNC et les descriptions des opérateurs
def get_mobile_mcc_mnc_codes():
    mobile_data = {
        "MCC": [208] * 19,
        "MNC": [1, 2, 10, 11, 13, 14, 15, 16, 20, 21, 22, 23, 24, 25, 26, 30, 33, 36, 88],
        "Operator": [
            "Orange", "Orange", "SFR", "SFR", "SFR", "Free Mobile", "Free Mobile", "Free Mobile",
            "Bouygues Telecom", "Bouygues Telecom", "Bouygues Telecom", "Bouygues Telecom", "Bouygues Telecom",
            "Lycamobile", "NRJ Mobile", "Altitude Télécom", "Omea Telecom", "Free Mobile", "Bouygues Telecom"
        ],
        "Description": [
            "Orange - Principal", "Orange - Réseau alternatif", "SFR - Principal", "SFR - Réseau alternatif", "SFR - Réseau alternatif",
            "Free Mobile - Principal", "Free Mobile - Réseau alternatif", "Free Mobile - Réseau alternatif",
            "Bouygues Telecom - Principal", "Bouygues Telecom - Réseau alternatif", "Bouygues Telecom - Réseau alternatif",
            "Bouygues Telecom - Réseau alternatif", "Bouygues Telecom - Réseau alternatif", "Lycamobile - MVNO",
            "NRJ Mobile - MVNO", "Altitude Télécom - MVNO", "Omea Telecom - MVNO", "Free Mobile - Réseau alternatif",
            "Bouygues Telecom - Réseau alternatif"
        ]
    }
    return mobile_data

# Charger les données du fichier CSV avec Dask
file_path = 'cell_towers_processed.csv'
ddf = dd.read_csv(file_path)

# Filtrer les données pour une région spécifique (par exemple, la France métropolitaine)
latitude_range = (43.0, 50.0)
longitude_range = (-1.5, 7.5)
filtered_ddf = ddf[(ddf['lat'] >= latitude_range[0]) & (ddf['lat'] <= latitude_range[1]) & 
                   (ddf['lon'] >= longitude_range[0]) & (ddf['mcc'] == 208)]

# Convertir le DataFrame Dask filtré en DataFrame Pandas
filtered_df = filtered_ddf.compute()

# Obtenir les informations sur les opérateurs
mobile_data = get_mobile_mcc_mnc_codes()
operator_info = { (mcc, mnc): (operator, description) 
                  for mcc, mnc, operator, description in 
                  zip(mobile_data['MCC'], mobile_data['MNC'], mobile_data['Operator'], mobile_data['Description']) }

# Initialiser la carte Folium
map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
marker_cluster = MarkerCluster().add_to(map)

# Ajouter des marqueurs pour chaque tour cellulaire
for index, row in filtered_df.iterrows():
    lat = row['lat']
    lon = row['lon']
    mcc = row['mcc']
    mnc = row['net']
    lac = row['area']
    cell_id = row['cell']
    
    operator, description = operator_info.get((mcc, mnc), ("Opérateur inconnu", "Pas de description disponible"))
    
    popup_text = f"MCC: {mcc}<br>MNC: {mnc}<br>Opérateur: {operator}<br>Description: {description}<br>LAC: {lac}<br>Cell ID: {cell_id}"
    folium.Marker(location=[lat, lon], popup=popup_text).add_to(marker_cluster)
    
# Sauvegarder la carte dans un fichier HTML
map.save('cell_towers_map2.html')
print("Carte de tours cellulaires créée : cell_towers_map.html")
