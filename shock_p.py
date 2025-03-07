# %%
import numpy as np 
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import newton

# %%
def velocityPlot(uDown,uUp,t,cl,pressure):
    plt.figure()
    plt.plot(t,uDown/cl,linestyle='dashed',label='Downstream')
    plt.xlabel(r'$t/(R_{0}/c_{L})$')
    plt.ylabel(r'$u/c_{L}$')
    plt.title(f'Velocity @ {pressure} MPa')
    plt.plot(t,uUp/cl,linestyle='solid',label='Upstream')
    plt.legend()
    plt.grid()
    plt.show()

# %%
def positionPlot(yDown,yUp,t,pressure,y0,r0):

    plt.figure()
    plt.plot(t,(yDown*r0)+y0,linestyle='dashed',label='Downstream')
    plt.xlabel(r'$t/(R_{0}/c_{L})$')
    plt.ylabel(r'$(y-y_{0})/R_{0}$')
    plt.title(f'Position @ {pressure} MPa')
    plt.plot(t,(yUp*r0)+y0,linestyle='solid',label='Upstream')
    plt.legend()
    plt.grid()
    plt.show()

# %%
def areaPlot(area,t,pressure,tKM,aKM):
    plt.figure()
    plt.plot(t,area,linestyle='solid',label='Simulation')
    plt.xlabel(r'$t/(R_{0}/c_{L})$')
    plt.ylabel(r'A/A0')
    plt.title(f' Area @ {pressure} MPa')
    plt.plot(tKM,aKM,linestyle='dashed',label='Keller-Miksis')
    plt.grid()
    plt.show()

# %%
def pressureContour(y,t,p,pressure,yd,yu,K=1001,y0=0.025,r0=0.000338):
    plt.figure()
    y=(y-y0)/r0
    pressureContour=plt.contourf(y,np.tile(t[:,None],(1,K)),p,cmap='jet')
    plt.colorbar(pressureContour,label='Pressure')
    plt.plot(yd,t,color='black')
    plt.plot(yu,t,color='black')
    plt.xlim(-2,2)
    plt.xlabel('Position along centerline (Y)')
    plt.ylabel('T')
    plt.title(f'Pressure Contour @ {pressure} MPa')
    plt.show()


# %%
def velocityContour(y,t,v,pressure,yd,yu,K=1001,y0=0.025,r0=0.000338):
    plt.figure()
    y=(y-y0)/r0
    pressureContour=plt.contourf(y,np.tile(t[:,None],(1,K)),v,cmap='jet')
    plt.colorbar(pressureContour,label='Pressure')
    plt.plot(yd,t,color='black')
    plt.plot(yu,t,color='black')
    plt.xlim(-2,2)
    plt.xlabel('Position along centerline (Y)')
    plt.ylabel('T')
    plt.title(f'Velocity Contour @ {pressure} MPa')
    plt.show()

# %%
def dataExtract(path,tc,pressure):
    #File Identification 
    M=len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]) #Number of files
    y0=0.025
    R0=0.000338
    K=1001
    #Array creation
    y=np.zeros((M,K))
    p = np.zeros((M, K))
    u = np.zeros((M, K))
    alpha = np.zeros((M, K))
    yInterfaceUpstream = np.zeros(((M,1)))
    uInterfaceUpstream = np.zeros(((M,1)))
    pInterfaceUpstream = np.zeros(((M,1)))
    yInterfaceDownstream = np.zeros(((M,1)))
    uInterfaceDownstream = np.zeros(((M,1)))
    pInterfaceDownstream = np.zeros(((M,1)))
    for i in range(M):
        file_path=f'{path}/line_{i}.csv'
        data=pd.read_csv(file_path)
        data =data.dropna()
        N=len(data)
        ytmp=data['Points_1'].to_numpy()
        alphatmp=data['diffuse volume fraction 1'].to_numpy()
        ptmp=data['pressure'].to_numpy()
        utmp=data['velocity_1'].to_numpy()
        dadx=np.zeros((N-2,1))
        Iarr=np.where(alphatmp>0.5)
        p[i,:]=ptmp
        u[i,:]=utmp
        y[i,:]=ytmp
        alpha[i,:]=alphatmp
        if(len(Iarr[0])==0):
            print(f'Jetting achieved for a pressure of:{pressure } MPa')
            break
        else:
            y_gas=ytmp[Iarr]
            ymax=np.max(y_gas)
            I=int(np.where(ytmp==ymax)[0][0])
            yInterfaceDownstream[i]=(ytmp[I]-y0)/R0
            uInterfaceDownstream[i]=utmp[I]
            pInterfaceDownstream[i]=ptmp[I]
            pInterfaceDownstream[i]=ptmp[I]

            #Downstream side
            ymin=np.min(y_gas)
            I=int(np.where(ytmp==ymin)[0][0])
            yInterfaceUpstream[i]=(ytmp[I]-y0)/R0
            uInterfaceUpstream[i]=utmp[I]
            pInterfaceUpstream[i]=ptmp[I]
    cl=1462
    R0=0.000338
    t=np.linspace(0,tc,M)
    t=t/(R0/cl)
    uInterfaceUpstream=np.trim_zeros(uInterfaceUpstream,'b')
    uInterfaceDownstream=np.trim_zeros(uInterfaceDownstream,'b')
    yInterfaceUpstream=yInterfaceUpstream[0:len(uInterfaceDownstream)]
    yInterfaceDownstream=yInterfaceDownstream[0:len(uInterfaceDownstream)]
    tJet=t[0:len(uInterfaceDownstream)]
    p=p[:len(uInterfaceDownstream),:]
    y=y[:len(uInterfaceDownstream),:]
    u=u[:len(uInterfaceDownstream),:]
    pressureContour(y,tJet,p,pressure,yInterfaceDownstream,yInterfaceUpstream)
    velocityContour(y,tJet,u,pressure,yInterfaceDownstream,yInterfaceUpstream)
    print(f'Final time recorded is:{t[-1]*(R0/cl)} s, for pressure of {pressure} MPa, the last simulated time is {tc} s')
    #velocityPlot(uInterfaceDownstream,uInterfaceUpstream,tJet,cl,pressure)
    #positionPlot(yInterfaceDownstream,yInterfaceUpstream,tJet,pressure,y0,R0)

# %%
def areaExtract(path,tc,pressure):
    M=len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))])
    R0=0.000338
    K=1001
    AreaAir=np.zeros(((M,1)))

    # Liquid
    rho   = 998
    pinf  = pressure*1e6
    c0    = np.sqrt(2.955*(pinf+7.22e8)/rho)

    # Gas bubble
    p0     = 1e5
    gamma  = 1.4
    sigma  = 0 # 0.073
    mu     = 0 # 1e-3
    pb0    = p0 + 2*sigma/R0
    rhob   = 1.2

    # Time
    tmax = tc
    t = np.linspace(0,tmax,M)
    def KM(y,t):
        R, R_dot = y
        P = pb0 * (R0/R)**(3*gamma) - 2*sigma/R - 4*mu*R_dot/R
        dpb_dt = (- pb0*(R0/R)**(3*gamma)*3*gamma/R*R_dot
              + 2*sigma/R**2*R_dot
              + 4*mu*R_dot**2/R**2
             )

        R_ddot = ( (P - pinf)/rho*(1+R_dot/c0)
               - 3/2*R_dot**2*(1-R_dot/(3*c0))
               + R*dpb_dt/(rho*c0)
             ) / ((1-R_dot/c0+4*mu/(rho*c0*R))*R)

        return [R_dot, R_ddot]
    def solve_KM():
        # Choice of initial condition. Not clearly defined for initial interface disequilibrium.
        y0 = [R0, -(pinf-pb0)/(rho*c0)]
        #y0 = [R0, 0]

        solution = odeint(KM, y0, t)

        return t, solution

    # Solve the KM equation
    t_sol, sol = solve_KM()
    for i in range(M):
        areaPath=f'{path}/lvlset_{i}.csv'
        areaDF=pd.read_csv(areaPath)
        alpha_vf=areaDF['diffuse volume fraction 1'].to_numpy()
        alpha_area=areaDF['Area'].to_numpy()
        AreaAir[i]=np.sum(alpha_area*alpha_vf)
    cl=1462
    collapseArr=np.abs((AreaAir-AreaAir[0])/AreaAir[0])
    collapse_idx=np.where(collapseArr>0.001)[0][0]
    A0=(np.pi*R0**2)/2
    t_sim=np.linspace(0,tc,M)
    t_sim=t_sim/(R0/cl)
    aKM=np.pi*0.5*sol[:,0]**2/A0
    t=t[collapse_idx:]
    aKM=aKM[0:len(t)]
    areaPlot(AreaAir/A0,t_sim,pressure,t/(R0/cl),aKM)

# %%
if __name__=="__main__":
    folders=['line_symaxi_data/LD_SS_20e6','line_symaxi_data/LD_WS_3e6','line_symaxi_data/LD_WS_1e6','line_symaxi_data/LD_WS_800e5','line_symaxi_data/LD_WS_700e5','line_symaxi_data/LD_WS_600e5','line_symaxi_data/LD_WS_500e5']
    areas=['volume_fractions/Area_SS_20e6','volume_fractions/Area_WS_3e6','volume_fractions/Area_WS_1e6','volume_fractions/Area_WS_800e5','volume_fractions/Area_WS_700e5','volume_fractions/Area_WS_600e5','volume_fractions/Area_WS_500e5']
    times=[6e-6,1.5e-5,2e-5,2.5e-5,3.5e-5,4e-5,5e-5]
    pressures=[20,3,1,0.8,0.7,0.6,0.5]
    for i in range(len(folders)):
        dataExtract(folders[i],times[i],pressures[i])
    #for i in range(len(areas)):
        #areaExtract(areas[i],times[i],pressures[i])


