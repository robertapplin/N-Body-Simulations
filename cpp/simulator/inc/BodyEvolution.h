// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#pragma once

#include "Body.h"

#include <map>
#include <memory>
#include <tuple>

namespace Simulator {

struct Vector2D;

// A mass, position and velocity of a body
using BodyState = std::tuple<double, Vector2D, Vector2D>;

// A class to store the masses, positions and velocities of a body over time.
class BodyEvolution {

public:
  BodyEvolution(double const mass, Vector2D position, Vector2D velocity);
  ~BodyEvolution();

  // Removes previously calculated masses, positions and velocities.
  void reset();

  // Add a mass, position and velocity for a specific time.
  void addTime(double const time, double const mass, Vector2D const position,
               Vector2D const velocity);

  // Returns the simulated evolutions of the body over time.
  [[nodiscard]] inline std::map<double, BodyState> const &
  timeEvolutions() const noexcept {
    return m_evolutions;
  }

private:
  // The evolution of the bodies state over time.
  std::map<double, BodyState> m_evolutions;
};

} // namespace Simulator
