from visit import *

DeleteAllPlots()
OpenDatabase(f"localhost:/data/home/exy214/phd/cavitation/jetting-ws-2025/dem/Runs/9MR/RayleighCollapse_L11/domain_0.*.xdmf database", 0)

# Add Plot and Operators
AddPlot("Pseudocolor", "diffuse volume fraction 1", 1, 1)
AddOperator("Slice", 1)

# Slice Attributes
SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Intercept
SliceAtts.originPoint = (0, 0, 0)
SliceAtts.normal = (0, 0, 1)
SliceAtts.axisType = SliceAtts.ZAxis
SliceAtts.project2d = 1
SetOperatorOptions(SliceAtts, 1, 1)

#Threshold Attributes
AddOperator("Threshold", 1)
ThresholdAtts = ThresholdAttributes()
ThresholdAtts.outputMeshType = 0
ThresholdAtts.boundsInputType = 0
ThresholdAtts.listedVarNames = ("default")
ThresholdAtts.zonePortions = (1)
ThresholdAtts.lowerBounds = (0.5)
ThresholdAtts.upperBounds = (1e+37)
ThresholdAtts.defaultVarName = "diffuse volume fraction 1"
ThresholdAtts.defaultVarIsScalar = 1
ThresholdAtts.boundsRange = ("0.5:1e+37")
SetOperatorOptions(ThresholdAtts, 2, 1)

DrawPlots()
nt=TimeSliderGetNStates()
f1=open(f"/data/home/exy214/phd/cavitation/jetting-ws-2025/dem/Runs/9MR/RayleighCollapse_L11/Area_L11.txt","w+")

for ts in range(0,nt):
	TimeSliderSetState(ts)
	time=Query("Time")
    t=GetQueryOutputValue()
    area=Query("2D Area")
    a=GetQueryOutputValue()
	f1.write("%15.12e %15.12e \n" % (t, a))
f1.close()
exit()
