from visit import *

DeleteAllPlots()
domain_folder='WS_100e6'
write_folder='volumeFrac_WS100e6'

OpenDatabase(f"localhost:/data/home/exy214/phd/cavitation/jetting-ws-2025/dem/Runs/{domain_folder}/domain/domain_0.*.xdmf database", 0)

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

#Annotation Attributes
AnnotationAtts = AnnotationAttributes()
# Disable all axes (2D and 3D)
AnnotationAtts.axes2D.visible = 0
AnnotationAtts.axesArray.visible = 0
# Disable axis titles and labels (2D and 3D)
AnnotationAtts.axes2D.xAxis.title.visible = 0
AnnotationAtts.axes2D.xAxis.label.visible = 0
AnnotationAtts.axes2D.yAxis.title.visible = 0
AnnotationAtts.axes2D.yAxis.label.visible = 0
# Disable grid lines (2D and 3D)
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.grid = 0
# Disable tick marks (2D and 3D)
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 0
# Disable background and other additional annotations
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 0
AnnotationAtts.legendInfoFlag = 0

# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-0.00214373, 0.00234967, 0.0241806, 0.0261377)
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
SaveWindowAtts.outputDirectory = f"/data/home/exy214/phd/cavitation/jetting-ws-2025/dem/Runs/{domain_folder}/domain/{write_folder}"
SaveWindowAtts.format = SaveWindowAtts.PNG   
SaveWindowAtts.height = 1024
SaveWindowAtts.width= 1024

for ts in range(0,nt):
	TimeSliderSetState(ts)
	SaveWindowAtts.fileName=f"schlieren"
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow()
