import numpy as np
import matplotlib.pyplot as plt
import os

class simulationRun:
    def __init__(self,filepath,pressure,tfinal,name):
        #Initial Stuff
        self.filepath=filepath
        self.pressure=pressure
        self.tfinal=tfinal
        self.name=name
        # For Area and Sphericity splots
        self.AreaArr=np.loadtxt(os.path.join(filepath, "Area.txt"))
        self.VolumeArr=np.loadtxt(os.path.join(filepath, "Volume.txt"))
        self.SurfaceAreaArr=np.loadtxt(os.path.join(filepath, "SurfaceArea.txt"))
        self.SphericityArr=np.column_stack((self.VolumeArr[:,0],(np.pi)**(1/3)*(6*self.VolumeArr[:,1])**(2/3)/(self.SurfaceAreaArr[:,1])))

        #For Pressure Matrix
        self.PressureTemplate = os.path.join(filepath, "pressure", "pressure{:04d}.txt")
        self.NumRuns = len(self.AreaArr)
        self.PressureList = [np.loadtxt(self.PressureTemplate.format(i)) for i in range(self.NumRuns)]
        self.PressureMatrix=np.stack(self.PressureList,axis=1)

        #For Velocity Matrix
        self.VelocityTemplate = os.path.join(filepath, "velocity", "velocity{:04d}.txt")
        self.NumRuns = len(self.AreaArr)
        self.VelocityList = [np.loadtxt(self.VelocityTemplate.format(i)) for i in range(self.NumRuns)]
        self.VelocityMatrix=np.stack(self.VelocityList,axis=1)

        #For Diffuse Volume Fraction Matrix
        self.AlphaTemplate = os.path.join(filepath, "alpha", "alpha{:04d}.txt")
        self.NumRuns = len(self.AreaArr)
        self.AlphaList = [np.loadtxt(self.AlphaTemplate.format(i)) for i in range(self.NumRuns)]
        self.AlphaMatrix=np.stack(self.AlphaList,axis=1)

        #For Position Matrix
        self.PositionMatrix=np.loadtxt(os.path.join(filepath,"pressure/position0000.txt"))+0.022 # Starts measuring from 0.022

        # Time Matrix
        self.tArray=np.linspace(0,tfinal,self.NumRuns)

        # Interface Values
        self.yInterfaceUpstream = np.zeros(((self.NumRuns,1)))
        self.uInterfaceUpstream = np.zeros(((self.NumRuns,1)))
        self.pInterfaceUpstream = np.zeros(((self.NumRuns,1)))
        self.yInterfaceDownstream = np.zeros(((self.NumRuns,1)))
        self.uInterfaceDownstream = np.zeros(((self.NumRuns,1)))
        self.pInterfaceDownstream = np.zeros(((self.NumRuns,1)))

        # Trimmed Interface Values
        self.TrimyInterfaceUpstream = np.zeros(((self.NumRuns,1)))
        self.TrimuInterfaceUpstream = np.zeros(((self.NumRuns,1)))
        self.TrimpInterfaceUpstream = np.zeros(((self.NumRuns,1)))
        self.TrimyInterfaceDownstream = np.zeros(((self.NumRuns,1)))
        self.TrimuInterfaceDownstream = np.zeros(((self.NumRuns,1)))
        self.TrimpInterfaceDownstream = np.zeros(((self.NumRuns,1)))
        self.TrimtArray = np.zeros(((self.NumRuns,1)))
        self.TrimPressureMatrix=np.zeros((self.NumRuns,len(self.PositionMatrix)))
        self.TrimVelocityMatrix=np.zeros((self.NumRuns,len(self.PositionMatrix)))
        self.TrimAlphaMatrix=np.zeros((self.NumRuns,len(self.PositionMatrix)))
        # Sadot Model
        self.AtwoodNumber=-1 # Atwood Number
        self.R0=0.000338 # Initial Radius

    def Sadot(self,t):
        # Calculate uj,0...
        A=self.AtwoodNumber
        k=(2**(1/2))*np.pi/self.R0
        uj0=2*65
        a0=(2-3**(1/2))*self.R0/2
        B=(1-abs(A))*abs(A)*(k**2)*uj0*a0
        C=(1-abs(A))*(1+abs(A))*3*(A**2)*(k**4)*(uj0**2)*(a0**2)/2
        uj_sadot=abs(A)*k*uj0*a0*(1+abs(A)*(k**2)*uj0*a0*t)/(1+B*t+C*(t**2))
        return uj_sadot
    def Interface(self):
        for i in range(self.NumRuns):
            Iarr=np.where(self.AlphaMatrix[:,i]>0.5)
            if(len(Iarr[0])==0):
                print(f'Jetting Achieved')
                break
            else:
                YGasPosition=self.PositionMatrix[Iarr]
                YMax=np.max(YGasPosition)
                I=int(np.where(self.PositionMatrix==YMax)[0][0])
                self.yInterfaceDownstream[i]=self.PositionMatrix[I]
                self.uInterfaceDownstream[i]=self.VelocityMatrix[:,i][I]
                self.pInterfaceDownstream[i]=self.PressureMatrix[:,i][I]

                YMin=np.min(YGasPosition)
                I=int(np.where(self.PositionMatrix==YMin)[0][0])
                self.yInterfaceUpstream[i]=self.PositionMatrix[I]
                self.uInterfaceUpstream[i]=self.VelocityMatrix[:,i][I]
                self.pInterfaceUpstream[i]=self.PressureMatrix[:,i][I]
    def CollapseTime(self):
        diffUpstream=np.diff(self.TrimuInterfaceUpstream.flatten())
        diffDownstream=np.diff(self.TrimuInterfaceDownstream.flatten())
        UpstreamCollapse=np.min(np.where(diffUpstream > 10))
        DownstreamCollapse=np.min(np.where(diffDownstream > 10))
        CollapseIdx=min(UpstreamCollapse,DownstreamCollapse)
        return CollapseIdx

    def TrimArrays(self):
        self.TrimuInterfaceUpstream=np.trim_zeros(self.uInterfaceUpstream,'b')
        self.TrimuInterfaceDownstream=np.trim_zeros(self.uInterfaceDownstream,'b')
        self.TrimyInterfaceUpstream=self.yInterfaceUpstream[0:len(self.TrimuInterfaceDownstream)]
        self.TrimyInterfaceDownstream=self.yInterfaceDownstream[0:len(self.TrimuInterfaceDownstream)]
        self.TrimtArray=self.tArray[0:len(self.TrimuInterfaceDownstream)]
        self.TrimPressureMatrix=self.PressureMatrix[:,:len(self.TrimuInterfaceDownstream)]
        self.TrimVelocityMatrix=self.VelocityMatrix[:,:len(self.TrimuInterfaceDownstream)]
        self.TrimAlphaMatrix=self.AlphaMatrix[:,:len(self.TrimuInterfaceDownstream)]

    def VelocityPlot(self):
        plt.figure()
        plt.plot(self.TrimtArray,self.TrimuInterfaceDownstream,'--',label='Downstream')
        plt.xlabel('Time (s)')
        plt.ylabel('u')
        plt.title(f'Velocity @ {self.pressure} MPa')
        plt.plot(self.TrimtArray,self.TrimuInterfaceUpstream,'--',label='Upstream')
        uj_sadot=self.Sadot(self.TrimtArray)
        Trimuj_sadot=np.concatenate([np.zeros(self.CollapseTime()+1),uj_sadot])[:len(uj_sadot)]
        plt.plot(self.TrimtArray,Trimuj_sadot,'--',label='Sadot Model')
        plt.legend()
        plt.savefig(os.path.join(self.filepath, f"VelocityPlot_{self.name}.png"))
    def PositionPlot(self):
        plt.figure()
        plt.plot(self.TrimtArray,self.TrimyInterfaceDownstream,linestyle='--',label='Downstream')
        plt.xlabel('Time (s)')
        plt.ylabel('u')
        plt.title(f'Position @ {self.pressure} MPa')
        plt.plot(self.TrimtArray,self.TrimyInterfaceUpstream,linestyle='--',label='Upstream')
        plt.legend()
        plt.savefig(os.path.join(self.filepath, f"PositionPlot_{self.name}.png"))
    def VelocityContour(self):
        plt.figure()
        velocityContour=plt.contourf(self.PositionMatrix.squeeze(), self.tArray, self.VelocityMatrix.T, cmap='jet')
        plt.colorbar(velocityContour,label='Velocity')
        plt.plot(self.TrimyInterfaceDownstream,self.TrimtArray,color='black')
        plt.plot(self.TrimyInterfaceUpstream,self.TrimtArray,color='black')
        plt.xlim(0.022,0.027)
        plt.xlabel('Position along centerline (y)')
        plt.ylabel('T')
        plt.title(f'Velocity contour @ {self.pressure} MPa')
        plt.savefig(os.path.join(self.filepath, f"VelocityContour_{self.name}.png"))
    def PressureContour(self):
        plt.figure()
        pressureContour=plt.contourf(self.PositionMatrix.squeeze(), self.tArray, self.PressureMatrix.T, cmap='jet')
        plt.colorbar(pressureContour,label='Pressure')
        plt.plot(self.TrimyInterfaceDownstream,self.TrimtArray,color='black')
        plt.plot(self.TrimyInterfaceUpstream,self.TrimtArray,color='black')
        plt.xlim(0.022,0.027)
        plt.xlabel('Position along centerline (y)')
        plt.ylabel('T')
        plt.title(f'Pressure contour @ {self.pressure} MPa')
        plt.savefig(os.path.join(self.filepath, f"PressureContour_{self.name}.png"))
    def AreaPlot(self):
        plt.figure()
        plt.plot(self.AreaArr[:,0],self.AreaArr[:,1]/self.AreaArr[0,1])
        plt.xlabel('Time (s)')
        plt.ylabel('Area (A/A0)')
        plt.title(f'Pressure @ {self.pressure} Pa')
        plt.savefig(os.path.join(self.filepath, f"AreaPlot_{self.name}.png"))
    def SphericityPlot(self):
        plt.figure()
        plt.plot(self.SphericityArr[:,0],self.SphericityArr[:,1])
        plt.xlabel('Time (s)')
        plt.ylabel('Sphericity')
        plt.title(f'Pressure @ {self.pressure} Pa')
        plt.savefig(os.path.join(self.filepath, f"SphericityPlot_{self.name}.png"))
    def PreProcessingWork(self):
        self.Interface()
        self.TrimArrays()
    def Run(self):
        self.PreProcessingWork()
        print('Plotting Area')
        self.AreaPlot()
        print('Plotting Sphericity')
        self.SphericityPlot()
        print('Plotting Interface Velocity')
        self.VelocityPlot()
        print('Plotting Interface Position')
        self.PositionPlot()
        print('Plotting Velocity Contour')
        self.VelocityContour()
        print('Plotting Pressure Contour')
        self.PressureContour()

if __name__=="__main__":
    WS100e6=simulationRun('/home/mrdsuser/Documents/cavitation/data/jetting_ws_2025/WS_100e6_Euler','100e6',5e-6,'WS100e6')
    WS100e6.Run()
    WS10e6=simulationRun('/home/mrdsuser/Documents/cavitation/data/jetting_ws_2025/WS_10e6_Euler','10e6',8e-6,'WS10e6')
    WS10e6.Run() 
    WS1e6=simulationRun('/home/mrdsuser/Documents/cavitation/data/jetting_ws_2025/WS_1e6','1e6',2e-5,'WS1e6')
    WS1e6.Run() 
    WS1e6Euler=simulationRun('/home/mrdsuser/Documents/cavitation/data/jetting_ws_2025/WS_1e6_Euler','1e6',2e-5,'WS1e6Euler')
    WS1e6Euler.Run()
    WS1e6ST=simulationRun('/home/mrdsuser/Documents/cavitation/data/jetting_ws_2025/WS_1e6_ST','1e6',2e-5,'WS1e6ST')
    WS1e6ST.Run()




  
