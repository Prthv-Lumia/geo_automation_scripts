from shapely.geometry import Polygon

poly1 = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
poly2 = Polygon([(1, 1), (3, 1), (3, 3), (1, 3)])

intersection = poly1.intersection(poly2)
print("Intersection area:", intersection.area)
print("Intersection WKT:", intersection.wkt)
