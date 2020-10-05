// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef SimulationConstants_H
#define SimulationConstants_H

namespace Simulator {
namespace Constants {

enum TimeUnit { Days } const;

static double G(6.67408e-11);       // Gravitational constant (m3 kg-1 s-2)
static double M_SOLAR(1.98847e+30); // Solar mass (kg)
static double AU(1.49598e+11);      // Astronomical unit (m)

static double DAY(60 * 60 * 24); // Day (s)

double gravitationalConstant(TimeUnit const &timeUnit);

} // namespace Constants
} // namespace Simulator

#endif // SimulationConstants_H
