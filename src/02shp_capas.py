import geopandas as gpd
import pandas as pd

layer = QgsVectorLayer(r"../data/eennpp.shp","Areas Protegidas")
layer2 = QgsVectorLayer(r"../data/zonas_protegidas2.shp","Areas Protegidas 2")
layers = [layer,layer2]
for index in range(len(layers)):
    QgsProject.instance().addMapLayer(layers[index])
