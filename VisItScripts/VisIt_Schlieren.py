from visit import *

domain_folders=['WS_100e6_Euler','WS_10e6_Euler','WS_1e6','WS_1e6_Euler','WS_1e6_ST','WS_500e5_Euler']
write_folders=['schlieren_WS100e6_Euler','schlieren_WS10e6_Euler','schlieren_WS1e6','schlieren_WS1e6_Euler','schlieren_WS1e6_ST','schlieren_WS500e5_Euler']

for domain_folder,write_folder in zip(domain_folders,write_folders):
  DeleteAllPlots()

  OpenDatabase(f"localhost:/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)

  # Add Plot and Operators
  AddPlot("Pseudocolor", "schlieren", 1, 1)
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

  PseudocolorAtts = PseudocolorAttributes()
  PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
  PseudocolorAtts.skewFactor = 1
  PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, ActualData
  PseudocolorAtts.minFlag = 0
  PseudocolorAtts.min = 0
  PseudocolorAtts.useBelowMinColor = 0
  PseudocolorAtts.belowMinColor = (0, 0, 0, 255)
  PseudocolorAtts.maxFlag = 1
  PseudocolorAtts.max = 1000000
  PseudocolorAtts.useAboveMaxColor = 0
  PseudocolorAtts.aboveMaxColor = (0, 0, 0, 255)
  PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
  PseudocolorAtts.colorTableName = "gray"
  PseudocolorAtts.invertColorTable = 1
  PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
  PseudocolorAtts.opacityVariable = ""
  PseudocolorAtts.opacity = 1
  PseudocolorAtts.opacityVarMin = 0
  PseudocolorAtts.opacityVarMax = 1
  PseudocolorAtts.opacityVarMinFlag = 0
  PseudocolorAtts.opacityVarMaxFlag = 0
  PseudocolorAtts.pointSize = 0.05
  PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
  PseudocolorAtts.pointSizeVarEnabled = 0
  PseudocolorAtts.pointSizeVar = "default"
  PseudocolorAtts.pointSizePixels = 2
  PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
  PseudocolorAtts.lineWidth = 0
  PseudocolorAtts.tubeResolution = 10
  PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
  PseudocolorAtts.tubeRadiusAbsolute = 0.125
  PseudocolorAtts.tubeRadiusBBox = 0.005
  PseudocolorAtts.tubeRadiusVarEnabled = 0
  PseudocolorAtts.tubeRadiusVar = ""
  PseudocolorAtts.tubeRadiusVarRatio = 10
  PseudocolorAtts.tailStyle = PseudocolorAtts.NONE  # NONE, Spheres, Cones
  PseudocolorAtts.headStyle = PseudocolorAtts.NONE  # NONE, Spheres, Cones
  PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
  PseudocolorAtts.endPointRadiusAbsolute = 0.125
  PseudocolorAtts.endPointRadiusBBox = 0.05
  PseudocolorAtts.endPointResolution = 10
  PseudocolorAtts.endPointRatio = 5
  PseudocolorAtts.endPointRadiusVarEnabled = 0
  PseudocolorAtts.endPointRadiusVar = ""
  PseudocolorAtts.endPointRadiusVarRatio = 10
  PseudocolorAtts.renderSurfaces = 1
  PseudocolorAtts.renderWireframe = 0
  PseudocolorAtts.renderPoints = 0
  PseudocolorAtts.smoothingLevel = 0
  PseudocolorAtts.legendFlag = 1
  PseudocolorAtts.lightingFlag = 1
  PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
  PseudocolorAtts.pointColor = (0, 0, 0, 0)
  SetPlotOptions(PseudocolorAtts)

  AnnotationAtts = AnnotationAttributes()
  AnnotationAtts.axes2D.visible = 0
  AnnotationAtts.axes2D.autoSetTicks = 1
  AnnotationAtts.axes2D.autoSetScaling = 1
  AnnotationAtts.axes2D.lineWidth = 0
  AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
  AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
  AnnotationAtts.axes2D.xAxis.title.visible = 1
  AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
  AnnotationAtts.axes2D.xAxis.title.font.scale = 1
  AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
  AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes2D.xAxis.title.font.bold = 1
  AnnotationAtts.axes2D.xAxis.title.font.italic = 1
  AnnotationAtts.axes2D.xAxis.title.userTitle = 0
  AnnotationAtts.axes2D.xAxis.title.userUnits = 0
  AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
  AnnotationAtts.axes2D.xAxis.title.units = ""
  AnnotationAtts.axes2D.xAxis.label.visible = 1
  AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
  AnnotationAtts.axes2D.xAxis.label.font.scale = 1
  AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
  AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes2D.xAxis.label.font.bold = 1
  AnnotationAtts.axes2D.xAxis.label.font.italic = 1
  AnnotationAtts.axes2D.xAxis.label.scaling = 0
  AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
  AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
  AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
  AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
  AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
  AnnotationAtts.axes2D.xAxis.grid = 0
  AnnotationAtts.axes2D.yAxis.title.visible = 1
  AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
  AnnotationAtts.axes2D.yAxis.title.font.scale = 1
  AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
  AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes2D.yAxis.title.font.bold = 1
  AnnotationAtts.axes2D.yAxis.title.font.italic = 1
  AnnotationAtts.axes2D.yAxis.title.userTitle = 0
  AnnotationAtts.axes2D.yAxis.title.userUnits = 0
  AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
  AnnotationAtts.axes2D.yAxis.title.units = ""
  AnnotationAtts.axes2D.yAxis.label.visible = 1
  AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
  AnnotationAtts.axes2D.yAxis.label.font.scale = 1
  AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
  AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes2D.yAxis.label.font.bold = 1
  AnnotationAtts.axes2D.yAxis.label.font.italic = 1
  AnnotationAtts.axes2D.yAxis.label.scaling = 0
  AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
  AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
  AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
  AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
  AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
  AnnotationAtts.axes2D.yAxis.grid = 0
  AnnotationAtts.axes3D.visible = 0
  AnnotationAtts.axes3D.autoSetTicks = 1
  AnnotationAtts.axes3D.autoSetScaling = 1
  AnnotationAtts.axes3D.lineWidth = 0
  AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
  AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
  AnnotationAtts.axes3D.triadFlag = 0
  AnnotationAtts.axes3D.bboxFlag = 0
  AnnotationAtts.axes3D.xAxis.title.visible = 1
  AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axes3D.xAxis.title.font.scale = 1
  AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
  AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes3D.xAxis.title.font.bold = 0
  AnnotationAtts.axes3D.xAxis.title.font.italic = 0
  AnnotationAtts.axes3D.xAxis.title.userTitle = 0
  AnnotationAtts.axes3D.xAxis.title.userUnits = 0
  AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
  AnnotationAtts.axes3D.xAxis.title.units = ""
  AnnotationAtts.axes3D.xAxis.label.visible = 1
  AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axes3D.xAxis.label.font.scale = 1
  AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
  AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes3D.xAxis.label.font.bold = 0
  AnnotationAtts.axes3D.xAxis.label.font.italic = 0
  AnnotationAtts.axes3D.xAxis.label.scaling = 0
  AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
  AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
  AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
  AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
  AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
  AnnotationAtts.axes3D.xAxis.grid = 0
  AnnotationAtts.axes3D.yAxis.title.visible = 1
  AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axes3D.yAxis.title.font.scale = 1
  AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
  AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes3D.yAxis.title.font.bold = 0
  AnnotationAtts.axes3D.yAxis.title.font.italic = 0
  AnnotationAtts.axes3D.yAxis.title.userTitle = 0
  AnnotationAtts.axes3D.yAxis.title.userUnits = 0
  AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
  AnnotationAtts.axes3D.yAxis.title.units = ""
  AnnotationAtts.axes3D.yAxis.label.visible = 1
  AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axes3D.yAxis.label.font.scale = 1
  AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
  AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes3D.yAxis.label.font.bold = 0
  AnnotationAtts.axes3D.yAxis.label.font.italic = 0
  AnnotationAtts.axes3D.yAxis.label.scaling = 0
  AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
  AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
  AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
  AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
  AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
  AnnotationAtts.axes3D.yAxis.grid = 0
  AnnotationAtts.axes3D.zAxis.title.visible = 1
  AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axes3D.zAxis.title.font.scale = 1
  AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
  AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes3D.zAxis.title.font.bold = 0
  AnnotationAtts.axes3D.zAxis.title.font.italic = 0
  AnnotationAtts.axes3D.zAxis.title.userTitle = 0
  AnnotationAtts.axes3D.zAxis.title.userUnits = 0
  AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
  AnnotationAtts.axes3D.zAxis.title.units = ""
  AnnotationAtts.axes3D.zAxis.label.visible = 1
  AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axes3D.zAxis.label.font.scale = 1
  AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
  AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
  AnnotationAtts.axes3D.zAxis.label.font.bold = 0
  AnnotationAtts.axes3D.zAxis.label.font.italic = 0
  AnnotationAtts.axes3D.zAxis.label.scaling = 0
  AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
  AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
  AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
  AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
  AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
  AnnotationAtts.axes3D.zAxis.grid = 0
  AnnotationAtts.axes3D.setBBoxLocation = 0
  AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
  AnnotationAtts.axes3D.triadColor = (0, 0, 0)
  AnnotationAtts.axes3D.triadLineWidth = 0
  AnnotationAtts.axes3D.triadFont = 0
  AnnotationAtts.axes3D.triadBold = 1
  AnnotationAtts.axes3D.triadItalic = 1
  AnnotationAtts.axes3D.triadSetManually = 0
  AnnotationAtts.userInfoFlag = 0
  AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
  AnnotationAtts.userInfoFont.scale = 1
  AnnotationAtts.userInfoFont.useForegroundColor = 1
  AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
  AnnotationAtts.userInfoFont.bold = 0
  AnnotationAtts.userInfoFont.italic = 0
  AnnotationAtts.databaseInfoFlag = 0
  AnnotationAtts.timeInfoFlag = 1
  AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
  AnnotationAtts.databaseInfoFont.scale = 1
  AnnotationAtts.databaseInfoFont.useForegroundColor = 1
  AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
  AnnotationAtts.databaseInfoFont.bold = 0
  AnnotationAtts.databaseInfoFont.italic = 0
  AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
  AnnotationAtts.databaseInfoTimeScale = 1
  AnnotationAtts.databaseInfoTimeOffset = 0
  AnnotationAtts.legendInfoFlag = 0
  AnnotationAtts.backgroundColor = (255, 255, 255, 255)
  AnnotationAtts.foregroundColor = (0, 0, 0, 255)
  AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
  AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
  AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
  AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
  AnnotationAtts.backgroundImage = ""
  AnnotationAtts.imageRepeatX = 1
  AnnotationAtts.imageRepeatY = 1
  AnnotationAtts.axesArray.visible = 1
  AnnotationAtts.axesArray.ticksVisible = 1
  AnnotationAtts.axesArray.autoSetTicks = 1
  AnnotationAtts.axesArray.autoSetScaling = 1
  AnnotationAtts.axesArray.lineWidth = 0
  AnnotationAtts.axesArray.axes.title.visible = 1
  AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axesArray.axes.title.font.scale = 1
  AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
  AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
  AnnotationAtts.axesArray.axes.title.font.bold = 0
  AnnotationAtts.axesArray.axes.title.font.italic = 0
  AnnotationAtts.axesArray.axes.title.userTitle = 0
  AnnotationAtts.axesArray.axes.title.userUnits = 0
  AnnotationAtts.axesArray.axes.title.title = ""
  AnnotationAtts.axesArray.axes.title.units = ""
  AnnotationAtts.axesArray.axes.label.visible = 1
  AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
  AnnotationAtts.axesArray.axes.label.font.scale = 1
  AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
  AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
  AnnotationAtts.axesArray.axes.label.font.bold = 0
  AnnotationAtts.axesArray.axes.label.font.italic = 0
  AnnotationAtts.axesArray.axes.label.scaling = 0
  AnnotationAtts.axesArray.axes.tickMarks.visible = 1
  AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
  AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
  AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
  AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
  AnnotationAtts.axesArray.axes.grid = 0
  SetAnnotationAttributes(AnnotationAtts)

  # Begin spontaneous state
  View2DAtts = View2DAttributes()
  View2DAtts.windowCoords = (-0.00225714, 0.00239977, 0.0233537, 0.0268101)
  View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
  View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
  View2DAtts.fullFrameAutoThreshold = 100
  View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
  View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
  View2DAtts.windowValid = 0
  SetView2D(View2DAtts)
  # End spontaneous state
  DrawPlots()

  nt=TimeSliderGetNStates()
  SaveWindowAtts = SaveWindowAttributes()
  SaveWindowAtts.outputToCurrentDirectory = 0
  SaveWindowAtts.outputDirectory = f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/{write_folder}"
  SaveWindowAtts.format = SaveWindowAtts.PNG   
  SaveWindowAtts.height = 1024
  SaveWindowAtts.width= 1024

  for ts in range(0,nt):
	  TimeSliderSetState(ts)
	  SaveWindowAtts.fileName=f"schlieren"
	  SetSaveWindowAttributes(SaveWindowAtts)
	  SaveWindow()
