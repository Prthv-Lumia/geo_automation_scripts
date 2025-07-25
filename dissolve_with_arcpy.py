import arcpy

# Set environment settings
arcpy.env.workspace = "C:/GIS_Project"
input_fc = "land_parcels.shp"
output_fc = "dissolved_parcels.shp"

# Dissolve based on 'LandUse' field
arcpy.Dissolve_management(input_fc, output_fc, "LandUse")
print("Dissolve completed.")
