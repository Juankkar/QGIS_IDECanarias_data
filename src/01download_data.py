import os
import pandas as pd
import requests

os.chdir('C:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\src')

metadata = pd.read_csv('C:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\metadata\\metadatos_medio_ambiente_shp.csv')
directorio_destino = 'C:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\data'

for url in list(metadata["url"]):
    try:
        # Obtener el nombre del archivo de la URL
        nombre_archivo = os.path.join(directorio_destino, os.path.basename(url))

        # Descargar el archivo
        response = requests.get(url)
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)

        print(f"Archivo descargado: {nombre_archivo}")
        
        # Descomprimir el archivo
        with zipfile.ZipFile(nombre_archivo_zip, 'r') as zip_ref:
            zip_ref.extractall(directorio_destino)
            print(f"Archivos descomprimidos en: {directorio_destino}")

    except Exception as e:
        print(f"Error al descargar {url}: {e}")
