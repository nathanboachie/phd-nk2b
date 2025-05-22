from visit import *
import numpy as np


domain_folders=['ColoniusL11']
write_folders=['volumeFrac_ColoniusL11']
for domain_folder,write_folder in zip(domain_folders,write_folders):

  DeleteAllPlots()
  OpenDatabase(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)

  # Add Plot and Operators
  AddPlot("Pseudocolor", "pressure", 1, 0)
  SetActivePlots(0)
  AddOperator("Reflect", 0)
  AddOperator("Slice", 0)

  # Reflect Attributes
  ReflectAtts = ReflectAttributes()
  ReflectAtts.octant = ReflectAtts.PXPYPZ  # Reflection type
  ReflectAtts.useXBoundary = 1
  ReflectAtts.specifiedX = 0
  ReflectAtts.useYBoundary = 0
  ReflectAtts.useZBoundary = 1
  ReflectAtts.specifiedZ = 0
  ReflectAtts.reflections = (1, 1, 0, 0, 0, 0, 0, 0)
  SetOperatorOptions(ReflectAtts, 0, 0)

  # Slice Attributes
  SliceAtts = SliceAttributes()
  SliceAtts.originType = SliceAtts.Intercept
  SliceAtts.originPoint = (0, 0, 0)
  SliceAtts.normal = (0, 0, 1)
  SliceAtts.axisType = SliceAtts.ZAxis
  SliceAtts.project2d = 1
  SetOperatorOptions(SliceAtts, 1, 0)

  #Pseudoclolor Attribtutes
  PseudocolorAtts=PseudocolorAttributes()
  PseudocolorAtts.colorTableName="YlGnBu"
  SetPlotOptions(PseudocolorAtts)

  AddPlot("Pseudocolor","schlieren",1,0)
  SetActivePlots(1)

  AddOperator("Slice",0)

  # Slice Attributes
  SliceAtts = SliceAttributes()
  SliceAtts.originType = SliceAtts.Intercept
  SliceAtts.originPoint = (0, 0, 0)
  SliceAtts.normal = (0, 0, 1)
  SliceAtts.axisType = SliceAtts.ZAxis
  SliceAtts.project2d = 1
  SetOperatorOptions(SliceAtts, 0, 0)

   #Pseudoclolor Attribtutes
  PseudocolorAtts=PseudocolorAttributes()
  PseudocolorAtts.min=0
  PseudocolorAtts.max=60000
  PseudocolorAtts.colorTableName="xray"
  SetPlotOptions(PseudocolorAtts)

  AnnotationAtts=AnnotationAttributes()
  AnnotationAtts.axes2D.visible=0
  AnnotationAtts.axes3D.visible=0
  AnnotationAtts.axesArray.visible=0

  AnnotationAtts.timeInfoFlag=0
  AnnotationAtts.databaseInfoFlag=0
  AnnotationAtts.userInfoFlag=0
  AnnotationAtts.legendInfoFlag=0
  SetAnnotationAttributes(AnnotationAtts)
  DrawPlots()

  # Begin spontaneous state
  View2DAtts = View2DAttributes()
  View2DAtts.windowCoords = (-0.0346989, 0.0346989, 0.0106235, 0.0793765)
  View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
  View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
  View2DAtts.fullFrameAutoThreshold = 100
  View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
  View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
  View2DAtts.windowValid = 1
  SetView2D(View2DAtts)

  # End spontaneous state

  nt=TimeSliderGetNStates()
  SaveWindowAtts = SaveWindowAttributes()
  SaveWindowAtts.outputToCurrentDirectory = 0
  SaveWindowAtts.outputDirectory = f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/{write_folder}"
  SaveWindowAtts.format = SaveWindowAtts.PNG
  SaveWindowAtts.height = 1024
  SaveWindowAtts.width= 1024

  for ts in range(0,nt):
    TimeSliderSetState(ts)
    SaveWindowAtts.fileName=f"volumeFrac"
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
exit()
