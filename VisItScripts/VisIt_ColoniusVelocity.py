from visit import *

domain_folders=['ColoniusL8','ColoniusL9','ColoniusL10','ColoniusL11']
pressures=['353e5','353e5','353e5','353e5']

for domain_folder,pressure in zip(domain_folders,pressures):
  DeleteAllPlots()
  OpenDatabase(f"localhost:/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)

  DefineScalarExpression('velocityY',"velocity[1]")
  OpenDatabase(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)
  AddPlot("Pseudocolor", "velocityY", 1, 1)
  DrawPlots()

  # Slice Attributes
  SliceAtts = SliceAttributes()
  SliceAtts.originType = SliceAtts.Intercept
  SliceAtts.originPoint = (0, 0, 0)
  SliceAtts.normal = (0, 0, 1)
  SliceAtts.axisType = SliceAtts.ZAxis
  SliceAtts.project2d = 1
  SetOperatorOptions(SliceAtts, 1, 1)

  DrawPlots()
  nt=TimeSliderGetNStates()
  f1=open(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/MaxVelocity_{pressure}.txt","w+")

  for ts in range(0,nt):
    TimeSliderSetState(ts)
    time=Query("Time")
    t=GetQueryOutputValue()
    velocity=Query("Max",use_actual_data=1)
    v=GetQueryOutputValue()
    f1.write("%15.12e %15.12e \n" % (t, v))
  f1.close()
exit()
