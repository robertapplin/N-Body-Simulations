// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/SimulationConstants.h"

#include <cmath>
#include <stdexcept>

namespace Simulator {
namespace Constants {

double gravitationalConstant(TimeUnit const &timeUnit) {
  switch (timeUnit) {
  case TimeUnit::Days:
    return G * M_SOLAR * pow(DAY, 2) * (1 / pow(AU, 3));
  }

  throw std::invalid_argument("An invalid time unit has been provided.");
}

} // namespace Constants
} // namespace Simulator
