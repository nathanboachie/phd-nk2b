from visit import *
import numpy as np

domain_folders=['ColoniusL11']
pressures=['353e5']

ActiveWindow1=1
ActiveWindow2=2
for domain_folder,name in zip(domain_folders,names):
  
  DeleteAllPlots()

  write_folder=f'alpha_{domain_folder}'

  OpenDatabase(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/domain_0.*.xdmf database", 0)
  AddPlot("Pseudocolor", "diffuse volume fraction 1", 1, 1)
  DrawPlots()
	
  SetActiveWindow(ActiveWindow1)
  nt=TimeSliderGetNStates()
  print(f"my number of states is: {nt}")
  
  for ts in range(0,nt):
      SetActiveWindow(ActiveWindow1) 
      TimeSliderSetState(ts)
      Lineout([0,0.022,0],[0,0.027,0],500)
      SetActiveWindow(ActiveWindow2)
      SetActivePlots(0)
      Data=GetPlotInformation()["Curve"]
      Alpha=Data[1::2]
      Position=Data[::2]
      np.savetxt(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/{write_folder}/alpha{ts:04d}.txt", Alpha)
      if ts == 0:
      	np.savetxt(f"/work/e01/e01/exy214/rdemic-dir/RDEMIC/{domain_folder}/domain/{write_folder}/position{ts:04d}.txt", Position)
  ActiveWindow1+=1
  ActiveWindow2+=1
