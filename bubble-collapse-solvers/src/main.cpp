#include <iostream>
#include "BubbleSolvers/RayleighSolver.hpp"
#include "BubbleSolvers/RPSolver.hpp"

int main(){
  //RayleighSolver RS{1000,1e6,1e5,0.000338};
  RPSolver RP{1000,500e5,1e5,0.0005,1.4,0,0};
  //RS.Run();
  RP.Run();
  return 0;
}
