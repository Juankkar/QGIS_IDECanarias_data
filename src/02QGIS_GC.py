import os
import geopandas as gpd

## ruta donde se encuentra el proyecto, incluyendo este
ruta_de_trabajo = "C:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\"
## Cambiamos la ubicación al direcotorio "source code"
os.chdir(f"{ruta_de_trabajo}src")

########################################
##    Leemos los datos vectoriales    ##
########################################

# Abrir el archivo existente como un GeoDataFrame
gfd_eennpp_gc = gpd.read_file("..\\data\\gran_canaria\\eennpp_gran_canaria.shp")

# Crear la nueva columna que se usará como etiquetas
gfd_eennpp_gc["etiquetas"] = gfd_eennpp_gc["codigo"] + "\n" + gfd_eennpp_gc["nombre_2"]

# Guardar el archivo en la misma ubicación con un nombre diferente
gfd_eennpp_gc.to_file("..\\data\\gran_canaria\\eennpp_gran_canaria_etiquetas.shp")

## Capas
gran_canaria_isla = QgsVectorLayer(r"..\\data\\gran_canaria\\gran_canaria_generalizada.shp","Gran Canaria Generalizado")
eennpp_gc = QgsVectorLayer(r"..\\data\\gran_canaria\\eennpp_gran_canaria_etiquetas.shp"," Red de Espacios Protegidos Naturales GC")
zec_zonificacion_gc = QgsVectorLayer(r"..\\data\\gran_canaria\\zec_zonificacion_gc.shp", "Zonificación ZEC GC")
zec_delimitacion_gc = QgsVectorLayer(r"..\\data\\unrar\\ZEC.shp", "Delimitación ZEC GC")

## Añadimos las capas a una lista
lista_capas = [gran_canaria_isla, 
               eennpp_gc, 
               zec_zonificacion_gc, 
               zec_delimitacion_gc]

## De la lista anterior descargamos las capas de vectores de los archivos SHP
for index in range(len(lista_capas)):
    QgsProject.instance().addMapLayer(lista_capas[index])