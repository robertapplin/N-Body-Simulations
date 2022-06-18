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

// A class used to store the positions and velocities of a body over time.
class BodyEvolution {

public:
  BodyEvolution(std::unique_ptr<Body> body);
  ~BodyEvolution();

  // Removes previously calculated positions and velocities.
  void resetParameters();

  // Return the body associated with the position and velocity coordinates.
  [[nodiscard]] Body &body() const;

  // Add a mass, position and velocity for a specific time.
  void addTime(double const time, double const mass, Vector2D const position,
               Vector2D const velocity);

  // Returns the simulated evolutions of the body over time.
  [[nodiscard]] inline std::map<double, BodyState> const &
  timeEvolutions() const noexcept {
    return m_evolutions;
  }

private:
  // The body related to the evolutions.
  std::unique_ptr<Body> m_body;
  // The evolution of the bodies state over time.
  std::map<double, BodyState> m_evolutions;
};

} // namespace Simulator
