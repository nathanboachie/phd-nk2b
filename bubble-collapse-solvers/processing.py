## Import Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Read CSV Files
Rayleigh=pd.read_csv('Rayleigh.csv')
Rayleigh_Plesset=pd.read_csv('Rayleigh_Plesset.csv')

##Plot Files
plt.plot(Rayleigh['Time'].to_numpy(),Rayleigh['Radius'].to_numpy(),label='Rayleigh Equation',color='red',linestyle='solid')
plt.plot(Rayleigh_Plesset['Time'].to_numpy(),Rayleigh_Plesset['Radius'].to_numpy(),label='Rayleigh Plesset Equation',linestyle='dashed')
plt.xlabel('tc/time')
plt.ylabel('R/R0')
plt.grid()
plt.legend()
plt.savefig('BubbleSolverPlot.png')