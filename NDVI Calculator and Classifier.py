Working NDVI Model.py

Type
Text
Size
3 KB (3,224 bytes)
Storage used
3 KB (3,224 bytes)
Location
Python Script
Owner
me
Modified
Jun 1, 2020 by me
Opened
Jun 1, 2020 by me
Created
Jun 1, 2020 with Google Drive Web
Add a description
Viewers can download
import arcpy

Input_Raster___Before_ = arcpy.GetParameterAsText(0)

Enter_Study_Area = arcpy.GetParameterAsText(1)

Use_Input_Features_for_Clipping_Geometry = arcpy.GetParameterAsText(2)
if Use_Input_Features_for_Clipping_Geometry == '#' or not Use_Input_Features_for_Clipping_Geometry:
    Use_Input_Features_for_Clipping_Geometry = "false" # provide a default value if unspecified

Input_signature_file = arcpy.GetParameterAsText(3)

Input_Red_Band_Raster__Before_ = arcpy.GetParameterAsText(4)

Input_Infrared_Band_Raster__Before_ = arcpy.GetParameterAsText(5)

Output_classified_raster__Before_ = arcpy.GetParameterAsText(6)

Output_NDVI_Raster__Before_ = arcpy.GetParameterAsText(7)

Input_Raster__After_ = arcpy.GetParameterAsText(8)

Input_Red_Band_Raster__After_ = arcpy.GetParameterAsText(9)

Input_Infrared_Band_Raster__After_ = arcpy.GetParameterAsText(10)

Output_classified_raster__After_ = arcpy.GetParameterAsText(11)

Output_NDVI_Raster__After_ = arcpy.GetParameterAsText(12)

NDVI_Difference = arcpy.GetParameterAsText(13)

# Local variables:
NoData_Value = "0"
Clipped_Raster = ""
Output_confidence_raster = ""
Clipped_Raster__2_ = ""
Output_confidence_raster__2_ = ""
Infrared_Band_Out__2_ = ""
Red_Band_Out__2_ = ""
Infrared_Band_Out = ""
Red_Band_Out = ""
NDVI_Variation = ""

arcpy.Clip_management(Input_Raster___Before_, "", Clipped_Raster, Enter_Study_Area, NoData_Value, Use_Input_Features_for_Clipping_Geometry, "NO_MAINTAIN_EXTENT")

arcpy.gp.MLClassify_sa("''", Input_signature_file, Output_classified_raster__Before_, "0.0", "EQUAL", "", Output_confidence_raster)

arcpy.Clip_management(Input_Raster__After_, "", Clipped_Raster__2_, Enter_Study_Area, NoData_Value, Use_Input_Features_for_Clipping_Geometry, "NO_MAINTAIN_EXTENT")

arcpy.gp.MLClassify_sa("''", Input_signature_file, Output_classified_raster__After_, "0.0", "EQUAL", "", Output_confidence_raster__2_)

arcpy.Clip_management(Input_Infrared_Band_Raster__After_, "", Infrared_Band_Out__2_, Enter_Study_Area, NoData_Value, Use_Input_Features_for_Clipping_Geometry, "NO_MAINTAIN_EXTENT")

arcpy.Clip_management(Input_Red_Band_Raster__After_, "", Red_Band_Out__2_, Enter_Study_Area, NoData_Value, Use_Input_Features_for_Clipping_Geometry, "NO_MAINTAIN_EXTENT")

arcpy.gp.RasterCalculator_sa("Float(\"%Infrared Band Out (2)%\" - \"%Red Band Out (2)%\") / Float(\"%Infrared Band Out (2)%\" + \"%Red Band Out (2)%\")", Output_NDVI_Raster__After_)

arcpy.Clip_management(Input_Infrared_Band_Raster__Before_, "", Infrared_Band_Out, Enter_Study_Area, NoData_Value, Use_Input_Features_for_Clipping_Geometry, "NO_MAINTAIN_EXTENT")

arcpy.Clip_management(Input_Red_Band_Raster__Before_, "", Red_Band_Out, Enter_Study_Area, NoData_Value, Use_Input_Features_for_Clipping_Geometry, "NO_MAINTAIN_EXTENT")

arcpy.gp.RasterCalculator_sa("Float(\"%Infrared Band Out%\" - \"%Red Band Out%\") / Float(\"%Infrared Band Out%\" + \"%Red Band Out%\")", Output_NDVI_Raster__Before_)

arcpy.gp.RasterCalculator_sa("\"%Output NDVI Raster (After)%\" - \"%Output NDVI Raster (Before)%\"", NDVI_Variation)

arcpy.gp.Reclassify_sa(NDVI_Variation, "", "-1 0 -1;0 0;0 1 1", NDVI_Difference, "DATA")
