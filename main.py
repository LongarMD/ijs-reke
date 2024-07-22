import geopandas as gpd

# Read the GML file
gml_file_path = 'data/reke1.gml'
gdf = gpd.read_file(gml_file_path)

# Display the GeoDataFrame
print(gdf)
