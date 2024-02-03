import geopandas as gpd
import numpy as np
import os

zonas_protegidas_canarias = gpd.read_file("c:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\data\\eennpp.shp")

zonas_protegidas_canarias["etiquetas"] = zonas_protegidas_canarias["codigo"] + "\n" + zonas_protegidas_canarias["nombre"]

zonas_protegidas_canarias.to_file("c:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\data\\eennpp_etiquetas.shp")

layer = QgsVectorLayer(r"c:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\data\\eennpp_etiquetas.shp","Areas Protegidas 2")

QgsProject.instance().addMapLayer(layer)

