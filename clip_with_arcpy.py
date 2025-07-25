import arcpy

in_features = "path/to/input.shp"
clip_features = "path/to/clip_boundary.shp"
out_feature_class = "path/to/output_clipped.shp"

arcpy.Clip_analysis(in_features, clip_features, out_feature_class)
print("Clipping completed!")