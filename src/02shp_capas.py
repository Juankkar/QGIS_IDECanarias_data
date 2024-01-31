orto_layer = QgsVectorLayer(r"\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\data\\orto_territorial_canarias\\orto_territorial_canarias.gpkg", "orto_territorial", "ogr")
QgsProject.instance().addMapLayer(orto_layer)

layer = QgsVectorLayer(r"C:\\Users\\jcge9\\Documents\\QGIS_IDECanarias_data\\data\\eennpp.shp","Areas Protegidas")
layers = [layer, layer2]
for index in range(len(layers)):
    QgsProject.instance().addMapLayer(layers[index])