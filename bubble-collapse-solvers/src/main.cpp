#include <iostream>
#include "BubbleSolvers/RayleighSolver.hpp"
#include "BubbleSolvers/RPSolver.hpp"

int main(){
  RayleighSolver RS{1000,500e5,1e5,500e-6};
  RPSolver RP{1000,500e5,1e5,500e-6,1.4,0.073,1e-3};
  RS.Run();
  RP.Run();
  return 0;
}
