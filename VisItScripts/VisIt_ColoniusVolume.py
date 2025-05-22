from visit import *

domain_folders=['ColoniusL11']
pressures=['353e5']

for domain_folder,pressure in zip(domain_folders,pressures):
  DeleteAllPlots()
  OpenDatabase(f"localhost:/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)
  print("Database loaded")
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

  AddOperator("Threshold", 1)
  ThresholdAtts = ThresholdAttributes()
  ThresholdAtts.outputMeshType = 0
  ThresholdAtts.boundsInputType = 0
  ThresholdAtts.listedVarNames = ("default")
  ThresholdAtts.zonePortions = (1)
  ThresholdAtts.lowerBounds = (0.1)
  ThresholdAtts.upperBounds = (1e+37)
  ThresholdAtts.defaultVarName = "diffuse volume fraction 1"
  ThresholdAtts.defaultVarIsScalar = 1
  ThresholdAtts.boundsRange = ("0.1:1e+37")
  SetOperatorOptions(ThresholdAtts, 2, 1)


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
  print("Opening file")
  f1=open(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/Volume_{pressure}.txt","w+")

  for ts in range(0,nt):
    TimeSliderSetState(ts)
    time=Query("Time")
    t=GetQueryOutputValue()
    area=Query("Weighted Variable Sum")
    a=GetQueryOutputValue()
    f1.write("%15.12e %15.12e \n" % (t, a))
    print("File written")
  f1.close()
exit()
