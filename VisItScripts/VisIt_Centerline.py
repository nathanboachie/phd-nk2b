from visit import *

domain_folders=['WS_100e6_Euler','WS_10e6_Euler','WS_1e6','WS_1e6_Euler','WS_1e6_ST','WS_500e5_Euler']
names=['WS100e6_Euler','WS10e6_Euler','WS1e6','WS1e6_Euler','WS1e6_ST','WS500e5_Euler']

for domain_folder,name in zip(domain_folders,names):
  outputs=['pressure','velocity','alpha']

  for item in outputs:
      DeleteAllPlots()

      output_variable=item
      write_folder=f'{output_variable}_{name}'
      write_variable=output_variable

      if output_variable=='alpha':
          write_variable = 'diffuse volume fraction 1'
      OpenDatabase(f"localhost:/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)
      AddPlot("Pseudocolor", write_variable, 1, 1)
      DrawPlots()

      nt=TimeSliderGetNStates()
      SaveWindowAtts = SaveWindowAttributes()
      SaveWindowAtts.outputToCurrentDirectory = 0
      SaveWindowAtts.family = 1
      SaveWindowAtts.outputDirectory = f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/{write_folder}"
      SaveWindowAtts.format = SaveWindowAtts.CURVE   
      SaveWindowAtts.height = 1024
      SaveWindowAtts.width= 1024
      SaveWindowAtts.fileName=f"{output_variable}"
      SetSaveWindowAttributes(SaveWindowAtts)

      for ts in range(0,nt):
          SetActiveWindow(1) 
          TimeSliderSetState(ts)
          Query("Lineout", end_point=[0,0.05,0], num_samples=50, start_point=[0,0,0], use_sampling=0)
          SetActiveWindow(2)
          SaveWindow()

# Everything in below comment works 100%
  '''
  DeleteAllPlots()

  domain_folder='WS_100e6'
  output_variable='pressure'
  write_folder=f'{output_variable}_WS100e6'
  write_variable=output_variable

  if output_variable=='alpha':

      write_variable = 'diffuse volume fraction 1'
  OpenDatabase(f"localhost:/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)
  AddPlot("Pseudocolor", write_variable, 1, 1)
  DrawPlots()



  nt=TimeSliderGetNStates()
  SaveWindowAtts = SaveWindowAttributes()
  SaveWindowAtts.outputToCurrentDirectory = 0
  SaveWindowAtts.family = 1
  SaveWindowAtts.outputDirectory = f"/data/home/exy214/phd/cavitation/jetting-ws-2025/dem/Runs/{domain_folder}/domain/{write_folder}"
  SaveWindowAtts.format = SaveWindowAtts.CURVE   
  SaveWindowAtts.height = 1024
  SaveWindowAtts.width= 1024
  SaveWindowAtts.fileName=f"{output_variable}"
  SetSaveWindowAttributes(SaveWindowAtts)

  for ts in range(0,nt):
      SetActiveWindow(1) 
      TimeSliderSetState(ts)
      Query("Lineout", end_point=[0,0.05,0], num_samples=50, start_point=[0,0,0], use_sampling=0)
      SetActiveWindow(2)
      SaveWindow()
  '''
