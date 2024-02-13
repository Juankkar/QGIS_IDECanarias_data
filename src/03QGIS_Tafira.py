import os
import geopandas as gpd

## ruta donde se encuentra el proyecto, incluyendo este
ruta_de_trabajo = "C:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\"
## Cambiamos la ubicación al direcotorio "source code"
os.chdir(f"{ruta_de_trabajo}src")

########################################
##    Leemos los datos vectoriales    ##
########################################

## Capas
eennpp_tafira = QgsVectorLayer(r"..\\data\\eennpp_tafira.shp","Paisaje Protegido de Tafira")
especies_protegiodas_tafira = QgsVectorLayer(r"..\\data\\especies_protegiodas_tafira.shp","Especies Protegidas de Tafira")

## Añadimos las capas a una lista
lista_capas = [eennpp_tafira, especies_protegiodas_tafira]

## De la lista anterior descargamos las capas de vectores de los archivos SHP
for index in range(len(lista_capas)):
    QgsProject.instance().addMapLayer(lista_capas[index])