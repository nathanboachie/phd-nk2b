from visit import *

domain_folders=['WS_100e6_Euler','WS_10e6_Euler','WS_1e6','WS_1e6_Euler','WS_1e6_ST','WS_500e5_Euler']
pressures=['100e6','10e6','1e6','1e6','1e6','500e5']
for domain_folder,pressure in zip(domain_folders,pressures):
  DeleteAllPlots()
  OpenDatabase(f"localhost:/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)

# Add Plot and Operators
  AddPlot("Pseudocolor", "diffuse volume fraction 1", 1, 1)
  AddOperator("Reflect", 1)
  AddOperator("Slice", 1)

# Reflect Attributes
  ReflectAtts = ReflectAttributes()
  ReflectAtts.octant = ReflectAtts.PXPYPZ  # Reflection type
  ReflectAtts.useXBoundary = 1
  ReflectAtts.specifiedX = 0
  ReflectAtts.useYBoundary = 0
  ReflectAtts.useZBoundary = 1
  ReflectAtts.specifiedZ = 0
  ReflectAtts.reflections = (1, 1, 0, 0, 0, 0, 0, 0)
  SetOperatorOptions(ReflectAtts, 0, 1)

# Slice Attributes
  SliceAtts = SliceAttributes()
  SliceAtts.originType = SliceAtts.Intercept
  SliceAtts.originPoint = (0, 0, 0)
  SliceAtts.normal = (0, 0, 1)
  SliceAtts.axisType = SliceAtts.ZAxis
  SliceAtts.project2d = 1
  SetOperatorOptions(SliceAtts, 1, 1)

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
  f1=open(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/Area_{pressure}.txt","w+")

  for ts in range(0,nt):
    TimeSliderSetState(ts)
    time=Query("Time")
    t=GetQueryOutputValue()
    area=Query("2D Area")
    a=GetQueryOutputValue()
    f1.write("%15.12e %15.12e \n" % (t, a))
  f1.close()
exit()
