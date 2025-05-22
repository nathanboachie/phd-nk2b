#pragma once

class RPSolver{
    private:
      double rho; //Liquid Density (kg/m**3)
      double p; //Pressure outside bubble (Pa)
      double p0; // Pressure inside bubble (Pa)
      double R0; // Initial Bubble Radius (m)
      double gamma; //Ratio of specific heat capacities
      double sigma; // Surface tension (N/m)
      double mu; //Dynamic viscosity (Pa s)
      double dt_euler=1e-9; //Euler Time steps
      double pb0;
      double pb;
      double tc_Rayleigh; //Collapse Time (s)
      int nt; //Number of time steps
      double* t=nullptr; //Time vector 
      double* r=nullptr; //Radius vector
      double* v=nullptr; //Velocity vector
      double* a=nullptr; //Acceleration vector
     
      void InitialiseVariables();
      void RSystem(double r, double rdot, double& dr_dt, double& drdot2_dt);
      void RK4Solver();
      void WriteSolution() const;
  
    public:
      RPSolver(double Rho,double P,double P0,double _R0,double Gamma, double Sigma, double Mu);
      ~RPSolver();
      void Run();
  };
