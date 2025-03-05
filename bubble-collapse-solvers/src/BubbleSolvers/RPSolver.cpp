#pragma once

#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <cstdlib>
#include "RPSolver.hpp"
/**
* @brief Initialises Variables which are more suitably done here than with constructor initialiser list
*/
void RPSolver::InitialiseVariables(){
    pb0=p0+2*sigma/R0;
    tc_Rayleigh=0.915*R0*std::sqrt(rho/(p-p0));
    nt=static_cast<double>(tc_Rayleigh/dt_euler);
    t=new double[nt];
    r=new double[nt];
    v=new double[nt];
    a=new double[nt];
    std::cout<<"There are " << nt<< " time steps, simulation completes at: "<<tc_Rayleigh<<" s"<<'\n';
}

/**
 * @brief Rayleigh System: Bubble collapse with a gas bubble, can have surface tension or visocisty 
 * @brief System is: rdotdot=(1/r)*((Pb-P)/(rho)-1.5*rdot**2) P = Liquid pressure, rho = Liquid density, P0 = bubble pressure, Pb = bubble pressure
 * @param r Radius 
 * @param rdot Velocity
 * @param dr_dt Position derivative 
 * @param drdot2_dt Velocity derivative 
 */
void RPSolver::RSystem(double r, double rdot, double& dr_dt, double& drdot2_dt)
{
    pb=pb0*std::pow((R0/r),3*gamma)-2*(sigma/r)-4*mu*(rdot/r);
    dr_dt=rdot;
    drdot2_dt=(1/r)*(((pb-p)/(rho))-1.5*std::pow(rdot,2));
}

/**
 * @brief Runge Kutta 4 Solver for System of ODEs. Already acts on an implemented system of ODEs.
 */
void RPSolver::RK4Solver(){
    double k1r;
    double k2r;
    double k3r;
    double k4r;
    double k1v;
    double k2v;
    double k3v;
    double k4v;
    for(int i=0;i<nt-1;i++){
    double h=dt_euler;
    RSystem(r[i],v[i],k1r,k1v);
    k1r*=h;
    k1v*=h;

    RSystem(r[i]+k1r/2,v[i]+k1v/2,k2r,k2v);
    k2r*=h;
    k2v*=h;

    RSystem(r[i]+k2r/2,v[i]+k2v/2,k3r,k3v);
    k3r*=h;
    k3v*=h;

    RSystem(r[i]+k3r/2,v[i]+k3v/2,k4r,k4v);
    k4r*=h;
    k4v*=h;

    r[i+1]=r[i]+((1.0/6.0)*k1r+(1.0/3.0)*k2r+(1.0/3.0)*k3r+(1.0/6.0)*k4r);
    v[i+1]=v[i]+((1.0/6.0)*k1v+(1.0/3.0)*k2v+(1.0/3.0)*k3v+(1.0/6.0)*k4v);
    t[i+1]=t[i]+h;
    }
    }
/**
 * @brief Writes non-dimensionalised solution to a csv file 
 */
void RPSolver::WriteSolution() const{
std::ofstream outputFile;
std::string filename="../Rayleigh_Plesset.csv";
outputFile.open(filename);
outputFile<<"Time"<<","<<"Radius"<<","<<"Velocity"<<std::endl;
for(int i=0;i<nt;i++){
    outputFile<<t[i]/tc_Rayleigh<<","<<r[i]/R0<<","<<v[i]<<std::endl;
}
outputFile.close();
}

/**
 * @brief Class constructor, will not run negative densities, pressures or radii given un-physical nature
 * @param Rho, User liquid density
 * @param P, User liquid pressure
 * @param P0, User cavity pressure
 * @param _R0, User initial bubble radius
 */
RPSolver::RPSolver(double Rho,double P,double P0,double _R0,double Gamma, double Sigma,double Mu)
    :rho{Rho}
    ,p{P}
    ,p0{P0}
    ,R0{_R0}
    ,gamma{Gamma}
    ,sigma{Sigma}
    ,mu{Mu}
    {
    if(Rho<0||P<0||p0<0||_R0<0) {
        std::cerr<<"Error, there is a negative density, pressure or radius!!"<<std::endl;
        std::exit(EXIT_FAILURE);
    }
    InitialiseVariables();
    }
/**
 * @brief Destructor. There should really be a better delete implementation.
 */
RPSolver::~RPSolver(){
    delete[] t;
    delete[] r;
    delete[] v;
    delete[] a;
}
/**
 * @brief Run function, initialises state vectors can runs Runge Kutta output, then writes solution to file
 * @brief For user to run solver
 */
void RPSolver::Run(){
    r[0]=R0;
    v[0]=0;
    t[0]=0;
    RK4Solver();
    WriteSolution();
}
