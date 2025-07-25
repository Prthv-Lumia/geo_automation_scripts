from shapely.geometry import Point
from shapely.ops import transform
import pyproj

point = Point(76.95, 8.52)  # lon, lat
buffer_meters = 1000  # 1 km buffer

# Projected transformation for buffer accuracy
project = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32643", always_xy=True).transform
inverse_project = pyproj.Transformer.from_crs("EPSG:32643", "EPSG:4326", always_xy=True).transform

projected_point = transform(project, point)
projected_buffer = projected_point.buffer(buffer_meters)
buffer_geom = transform(inverse_project, projected_buffer)

print(buffer_geom)