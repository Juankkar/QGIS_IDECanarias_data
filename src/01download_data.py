import os
import geopandas as gpd
import pandas as pd
import zipfile
import requests
import fiona

#################################
##    Descarga de los datos    ##
#################################

## ruta donde se encuentra el proyecto, incluyendo este
ruta_de_trabajo = "C:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\"
## Cambiamos la ubicación al direcotorio "source code"
os.chdir(f"{ruta_de_trabajo}src")

metadata = pd.read_csv('..\\metadata\\metadatos_medio_ambiente_shp.csv')
directorio_destino = '..\\data'

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
        with zipfile.ZipFile(nombre_archivo, 'r') as zip_ref:
            zip_ref.extractall(directorio_destino)
            print(f"Archivos descomprimidos en: {directorio_destino}")

    except Exception as e:
        print(f"Error al descargar {url}: {e}")

########################################
##    Leemos los datos vectoriales    ##
########################################

## Capas
areas_protegidas = QgsVectorLayer(r"..\\data\\eennpp.shp","Areas Protegidas")

## Añadimos las capas a una lista
lista_capas = [areas_protegidas]

## De la lista anterior descargamos las capas de vectores de los archivos SHP
for index in range(len(lista_capas)):
    QgsProject.instance().addMapLayer(lista_capas[index])

##############################################################
##    Modificamos la tabla de atributos usando GeoPandas    ##
##############################################################

## Queremos crear una nueva columna en la tabla de valores que nos 
## que consiste en la suma de la columna "Código" + "nombre" (nombre
## del lugar). Para ello usaremos la librería GeoPandas

# Abrir el archivo existente como un GeoDataFrame
areas_protegidas_gdf = gpd.read_file("..\\data\\eennpp.shp")

# Crear la nueva columna que se usará como etiquetas
areas_protegidas_gdf["etiquetas"] = areas_protegidas_gdf["codigo"] + "\n" + areas_protegidas_gdf["nombre"]

# Guardar el archivo en la misma ubicación con un nombre diferente
areas_protegidas_gdf.to_file('..\\data\\eennpp2.shp')  

######################################################
##    Leemos los datos vectoriales con etiquetas    ##
######################################################

## Capas
areas_protegidas2 = QgsVectorLayer(r"..\\data\\eennpp2.shp","Areas Protegidas 2")

## Añadimos las capas a una lista
lista_capas2 = [areas_protegidas2]

## De la lista anterior descargamos las capas de vectores de los archivos SHP
for index in range(len(lista_capas2)):
    QgsProject.instance().addMapLayer(lista_capas2[index])
