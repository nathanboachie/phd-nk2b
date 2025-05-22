#pragma once

class RayleighSolver{
    private:
      double rho; //Liquid Density (kg/m**3)
      double p; //Pressure outside bubble (Pa)
      double p0; // Pressure inside bubble (Pa)
      double R0; // Initial Bubble Radius (m)
      double dt_euler=1e-9; //Euler Time steps
      double B;
      double tc_Rayleigh; //Collapse Time (s)
      int nt; //Number of time steps
      double* t=nullptr; //Time vector 
      double* r=nullptr; //Radius vector
      double* v=nullptr; //Velocity vector
      double* a=nullptr; //Acceleration vector
     
      void InitialiseVariables();
      void RSystem(double r, double rdot, double& dr_dt, double& drdot2_dt, double beta);
      void RK4Solver();
      void WriteSolution() const;
  
    public:
      RayleighSolver(double Rho,double P,double P0,double _R0);
      ~RayleighSolver();
      void Run();
  };