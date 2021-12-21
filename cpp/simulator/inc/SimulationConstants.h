// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef SimulationConstants_H
#define SimulationConstants_H

namespace Simulator {
namespace Constants {

enum TimeUnit { Days };

static double G(6.67408e-11);       // Gravitational constant (m3 kg-1 s-2)
static double M_SOLAR(1.98847e+30); // Solar mass (kg)
static double AU(1.49598e+11);      // Astronomical unit (m)

static double DAY(60.0 * 60.0 * 24.0); // Day (s)

// Calculates the gravitational constant for the specified time unit.
[[nodiscard]] double gravitationalConstant(TimeUnit const &timeUnit);

// Returns a pseudo value to use for the density of a body. These densities are
// not based in reality.
[[nodiscard]] double density(double const mass);

} // namespace Constants
} // namespace Simulator

#endif // SimulationConstants_H
