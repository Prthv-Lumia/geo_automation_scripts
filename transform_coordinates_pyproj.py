from pyproj import Transformer

# Define transformer from WGS84 to UTM Zone 43N
transformer = Transformer.from_crs("EPSG:4326", "EPSG:32643", always_xy=True)

lon, lat = 76.95, 8.52
x, y = transformer.transform(lon, lat)
print(f"UTM Coordinates: X = {x}, Y = {y}")