from visit import *

DeleteAllPlots()
domain_folder='WS_100e6'
pressure='WS100e6'
OpenDatabase(f"localhost:/data/home/exy214/phd/cavitation/jetting-ws-2025/dem/Runs/{domain_folder}/domain/domain_0.*.xdmf database", 0)

# Add Plot and Operators
AddPlot("Pseudocolor", "diffuse volume fraction 1", 1, 1)
AddOperator("Slice", 1)

#Slice Attributes
SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Intercept
SliceAtts.originPoint = (0, 0, 0)
SliceAtts.normal = (0, 0, 1)
SliceAtts.axisType = SliceAtts.ZAxis
SliceAtts.project2d = 1
SetOperatorOptions(SliceAtts, 1, 1)

AddOperator("Isosurface", 1)
IsosurfaceAtts = IsosurfaceAttributes()
IsosurfaceAtts.contourNLevels = 10
IsosurfaceAtts.contourValue = (0.5)
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
IsosurfaceAtts.minFlag = 0
IsosurfaceAtts.min = 0
IsosurfaceAtts.maxFlag = 0
IsosurfaceAtts.max = 1
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "default"
SetOperatorOptions(IsosurfaceAtts, 1, 1)

#Revolve Attribtue
AddOperator("Revolve", 1)
RevolveAtts = RevolveAttributes()
RevolveAtts.meshType = RevolveAtts.ZR  # Auto, XY, RZ, ZR
RevolveAtts.autoAxis = 1
RevolveAtts.axis = (1, 0, 0)
RevolveAtts.startAngle = 0
RevolveAtts.stopAngle = 360
RevolveAtts.steps = 120
SetOperatorOptions(RevolveAtts, 2, 1)

DrawPlots()
nt=TimeSliderGetNStates()

f1=open(f"/data/home/exy214/phd/cavitation/jetting-ws-2025/dem/Runs/{domain_folder}/domain/SurfaceArea_{pressure}.txt","w+")

for ts in range(0,nt):
	TimeSliderSetState(ts)
	time=Query("Time")
    t=GetQueryOutputValue()
    area=Query("3D surface area")
    a=GetQueryOutputValue()
	f1.write("%15.12e %15.12e \n" % (t, a))
f1.close()
exit()
