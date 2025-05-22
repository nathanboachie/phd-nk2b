from visit import *

domain_folders=['WS_100e6_Euler','WS_10e6_Euler','WS_1e6','WS_1e6_Euler','WS_1e6_ST','WS_500e5_Euler']
pressures=['100e6','10e6','1e6','1e6','1e6','500e5']

for domain_folder,pressure in zip(domain_folders,pressures):
  DeleteAllPlots()
  OpenDatabase(f"localhost:/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)

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

  f1=open(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/SurfaceArea_{pressure}.txt","w+")

  for ts in range(0,nt):
    TimeSliderSetState(ts)
    time=Query("Time")
    t=GetQueryOutputValue()
    area=Query("3D surface area")
    a=GetQueryOutputValue()
    f1.write("%15.12e %15.12e \n" % (t, a))
  f1.close()
  exit()
