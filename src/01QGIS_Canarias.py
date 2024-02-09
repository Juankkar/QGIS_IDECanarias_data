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
islas_canarias = QgsVectorLayer(r"..\\data\\islas_generalizadas.shp","Islas Generalizadas")
areas_protegidas = QgsVectorLayer(r"..\\data\\eennpp.shp","Areas Protegidas")

## Añadimos las capas a una lista
lista_capas = [islas_canarias, areas_protegidas]

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
