import requests
import pandas as pd
import gzip
import io

# Remplacez par votre clé API OpenCellID
api_key = ' '

# URL pour télécharger les données des tours cellulaires
url = f'https://opencellid.org/ocid/downloads?token={api_key}&file=cell_towers.csv.gz'

# Télécharger les données
response = requests.get(url)
if response.status_code == 200:
    with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as f:
        df = pd.read_csv(f)

    # Afficher les premières lignes du DataFrame
    print(df.head())

    # Sauvegarder le DataFrame en CSV
    df.to_csv('cell_towers_processed.csv', index=False)

    print("Données des tours cellulaires téléchargées et sauvegardées.")
else:
    print("Erreur lors du téléchargement des données.")
