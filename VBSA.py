# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# VBSA.py
# Created on: 2021-04-05 23:51:11.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: VBSA <Input_Urban_Settlements> <Inpur_Existing_Facilities> <Input_Population__Infected_Population_Combined> <Input_AIr__Heliports> <Input_Reserved_Vegetation> <Input_Roads> <Input_Clip_Feature> <Suitable_Areas> 
# Description: 
# A model to perform Vector Based Suitability Analysis prepared as part of completion of Geographic Information System Specialization by UCDavis. 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Input_Urban_Settlements = arcpy.GetParameterAsText(0)

Inpur_Existing_Facilities = arcpy.GetParameterAsText(1)

Input_Population__Infected_Population_Combined = arcpy.GetParameterAsText(2)

Input_AIr__Heliports = arcpy.GetParameterAsText(3)

Input_Reserved_Vegetation = arcpy.GetParameterAsText(4)

Input_Roads = arcpy.GetParameterAsText(5)

Input_Clip_Feature = arcpy.GetParameterAsText(6)

Suitable_Areas = arcpy.GetParameterAsText(7)
if Suitable_Areas == '#' or not Suitable_Areas:
    Suitable_Areas = "C:\\Users\\Pr4ntoR\\Documents\\ArcGIS\\Default.gdb\\rastercalc" # provide a default value if unspecified

# Local variables:
Existing_Facilities = ""
Output_cell_size = "100"
Output_direction_raster = ""
Air__Heliports = ""
Output_direction_raster__2_ = ""
Urban_Settlements = ""
Output_direction_raster__3_ = ""
Reserved_Vegetation = ""
Output_direction_raster__4_ = ""
SQL___Select_Major_Roads = ""
Roads = ""
Output_direction_raster__5_ = ""
Set_Infected_Population_Visible_Only = ""
Input_Infected_Population = ""
Infected_Population = ""
Output_direction_raster__6_ = ""
Set_Population_Visible_Only = ""
Input_Population = ""
Population = ""
Distance___Existing_Facilities__7_ = ""
Distance___Population = ""
Raster___Population = ""
Reclass_field = ""
Reclassification_Input___Population = ""
Reclass___Population = ""
Distance___Infected_Population = ""
Raster___Infected_Population = ""
Reclassification_Input___Infected_Population = ""
Reclass___Infected_Population = ""
Distance___Roads = ""
Raster___Roads = ""
Reclassification_Input___Roads = ""
Reclass___Roads = ""
Distance___Urban_Settlements = ""
Raster___Urban_Settlements = ""
Reclassification_Input___Urban_Settlements = ""
Reclass___Urban_Settlements = ""
Distance___Existing_Facilities = ""
Raster___Existing_Features = ""
Reclassification_Input___Existing_Facilities = ""
Reclass___Existing_Facilities = ""
Distance___Reserved_Vegetation = ""
Raster___Reserved_Vegetation = ""
Reclassification_Input___Reserved_Vegetation = ""
Reclass___Reserved_Vegetation = ""
Distance___Air__Heli_Ports = ""
Raster___Air__Heli_Ports = ""
Reclassification_Input___Air__Heli_Ports = ""
Reclass___Air__Heli_Ports = ""

# Process: Clip - Existing Facilities
arcpy.Clip_analysis(Inpur_Existing_Facilities, Input_Clip_Feature, Existing_Facilities, "")

# Process: Euclidean Distance - Existing Features
arcpy.gp.EucDistance_sa(Existing_Facilities, Distance___Existing_Facilities, "", Output_cell_size, Output_direction_raster)

# Process: Clip - Air/ Heliports
arcpy.Clip_analysis(Input_AIr__Heliports, Input_Clip_Feature, Air__Heliports, "")

# Process: Euclidean Distance - Air/ Heli Ports
arcpy.gp.EucDistance_sa(Air__Heliports, Distance___Air__Heli_Ports, "", Output_cell_size, Output_direction_raster__2_)

# Process: Clip - Urban Settlement
arcpy.Clip_analysis(Input_Urban_Settlements, Input_Clip_Feature, Urban_Settlements, "")

# Process: Euclidean Distance - Urban Settlements
arcpy.gp.EucDistance_sa(Urban_Settlements, Distance___Urban_Settlements, "", Output_cell_size, Output_direction_raster__3_)

# Process: Clip - Reserved Vegetation
arcpy.Clip_analysis(Input_Reserved_Vegetation, Input_Clip_Feature, Reserved_Vegetation, "")

# Process: Euclidean Distance - Reserved Vegetation
arcpy.gp.EucDistance_sa(Reserved_Vegetation, Distance___Reserved_Vegetation, "", Output_cell_size, Output_direction_raster__4_)

# Process: Select Major Roads
arcpy.MakeFeatureLayer_management("", Input_Roads, SQL___Select_Major_Roads, "", "")

# Process: Clip - Road
arcpy.Clip_analysis(Input_Roads, Input_Clip_Feature, Roads, "")

# Process: Euclidean Distance - Roads
arcpy.gp.EucDistance_sa(Roads, Distance___Roads, "", Output_cell_size, Output_direction_raster__5_)

# Process: Make Infected Population Feature
arcpy.MakeFeatureLayer_management(Input_Population__Infected_Population_Combined, Input_Infected_Population, "", "", Set_Infected_Population_Visible_Only)

# Process: Clip - Infected Population
arcpy.Clip_analysis(Input_Infected_Population, Input_Clip_Feature, Infected_Population, "")

# Process: Euclidean Distance - Infected Population
arcpy.gp.EucDistance_sa(Infected_Population, Distance___Infected_Population, "", Output_cell_size, Output_direction_raster__6_)

# Process: Make Population Feature
arcpy.MakeFeatureLayer_management(Input_Population__Infected_Population_Combined, Input_Population, "", "", Set_Population_Visible_Only)

# Process: Clip - Population
arcpy.Clip_analysis(Input_Population, Input_Clip_Feature, Population, "")

# Process: Euclidean Distance - Population
arcpy.gp.EucDistance_sa(Population, Distance___Existing_Facilities__7_, "", Output_cell_size, Distance___Population)

# Process: Clip - Raster - Population
arcpy.Clip_management(Distance___Population, "", Raster___Population, Input_Clip_Feature, "", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Reclassify - Population
arcpy.gp.Reclassify_sa(Raster___Population, Reclass_field, Reclassification_Input___Population, Reclass___Population, "DATA")

# Process: Clip - Raster - Infecteed Population
arcpy.Clip_management(Distance___Infected_Population, "", Raster___Infected_Population, Input_Clip_Feature, "", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Reclassify - Infected Poplation
arcpy.gp.Reclassify_sa(Raster___Infected_Population, Reclass_field, Reclassification_Input___Infected_Population, Reclass___Infected_Population, "DATA")

# Process: Clip - Raster - Roads
arcpy.Clip_management(Distance___Roads, "", Raster___Roads, Input_Clip_Feature, "", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Reclassify - Roads
arcpy.gp.Reclassify_sa(Raster___Roads, Reclass_field, Reclassification_Input___Roads, Reclass___Roads, "DATA")

# Process: Clip - Raster - Urban Settlements
arcpy.Clip_management(Distance___Urban_Settlements, "", Raster___Urban_Settlements, Input_Clip_Feature, "", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Reclassify - Urban Settlements
arcpy.gp.Reclassify_sa(Raster___Urban_Settlements, Reclass_field, Reclassification_Input___Urban_Settlements, Reclass___Urban_Settlements, "DATA")

# Process: Clip - Raster - Existing Facilities
arcpy.Clip_management(Distance___Existing_Facilities, "", Raster___Existing_Features, Input_Clip_Feature, "", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Reclassify - Existing Facilities
arcpy.gp.Reclassify_sa(Raster___Existing_Features, Reclass_field, Reclassification_Input___Existing_Facilities, Reclass___Existing_Facilities, "DATA")

# Process: Clip - Raster - Reserved Vegetation
arcpy.Clip_management(Distance___Reserved_Vegetation, "", Raster___Reserved_Vegetation, Input_Clip_Feature, "", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Reclassify - Reserved Vegetation
arcpy.gp.Reclassify_sa(Raster___Reserved_Vegetation, Reclass_field, Reclassification_Input___Reserved_Vegetation, Reclass___Reserved_Vegetation, "DATA")

# Process: Clip - Raster - Air/ Heli Ports
arcpy.Clip_management(Distance___Air__Heli_Ports, "", Raster___Air__Heli_Ports, Input_Clip_Feature, "", "NONE", "NO_MAINTAIN_EXTENT")

# Process: Reclassify - Air/ Heli Ports
arcpy.gp.Reclassify_sa(Raster___Air__Heli_Ports, Reclass_field, Reclassification_Input___Air__Heli_Ports, Reclass___Air__Heli_Ports, "DATA")

# Process: Raster Calculator
arcpy.gp.RasterCalculator_sa("\"%Reclass - Population%\" + \"%Reclass - Infected Population%\" + \"%Reclass - Roads%\" + \"%Reclass - Urban Settlements%\" + \"%Reclass - Existing Facilities%\" + \"%Reclass - Reserved Vegetation%\" + \"%Reclass - Air/ Heli Ports%\"", Suitable_Areas)
