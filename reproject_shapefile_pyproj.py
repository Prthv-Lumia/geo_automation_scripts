from pyproj import Transformer
import shapefile

# Transformer from EPSG:4326 to EPSG:3857
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)

# Read input shapefile
r = shapefile.Reader("points_wgs84.shp")
w = shapefile.Writer("points_webmercator.shp")
w.fields = r.fields[1:]

for rec, shape in zip(r.records(), r.shapes()):
    x, y = transformer.transform(shape.points[0][0], shape.points[0][1])
    w.point(x, y)
    w.record(*rec)

w.close()
print("Reprojection completed.")
