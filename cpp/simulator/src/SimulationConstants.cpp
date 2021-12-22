// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "SimulationConstants.h"

#include <cmath>
#include <stdexcept>

namespace Simulator {
namespace Constants {

double const gravitationalConstant(TimeUnit const &timeUnit) {
  switch (timeUnit) {
  case TimeUnit::Days:
    return G * M_SOLAR * pow(DAY, 2) * (1.0 / pow(AU, 3));
  }

  throw std::invalid_argument("An invalid time unit has been provided.");
}

double const density(double const mass) {
  double densityKgPerMetreCubed;
  if (mass <= 0.0001)
    densityKgPerMetreCubed = 0.1;
  else if (mass <= 0.001)
    densityKgPerMetreCubed = 0.2;
  else if (mass <= 0.01)
    densityKgPerMetreCubed = 0.3;
  else if (mass <= 0.1)
    densityKgPerMetreCubed = 0.4;
  else if (mass <= 1.0)
    densityKgPerMetreCubed = 0.5;
  else if (mass <= 10.0)
    densityKgPerMetreCubed = 0.6;
  else
    densityKgPerMetreCubed = 0.7;
  return densityKgPerMetreCubed * pow(AU, 3) * (1.0 / M_SOLAR);
}

} // namespace Constants
} // namespace Simulator
