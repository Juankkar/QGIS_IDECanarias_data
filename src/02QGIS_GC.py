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
gran_canaria_isla = QgsVectorLayer(r"..\\data\\gran_canaria_isla.shp","Gran Canaria Generalizado")
gc_muni = QgsVectorLayer(r"..\\data\\gc_municipios.shp","Gran Canaria Municipios")
eennpp_gc = QgsVectorLayer(r"..\\data\\eennp_gran_canaria.shp","eennpp Gran Canaria")

## Añadimos las capas a una lista
lista_capas = [gran_canaria_isla, gc_muni, eennpp_gc]

## De la lista anterior descargamos las capas de vectores de los archivos SHP
for index in range(len(lista_capas)):
    QgsProject.instance().addMapLayer(lista_capas[index])