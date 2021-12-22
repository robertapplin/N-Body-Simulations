// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef SpaceTimeBodyCoords_H
#define SpaceTimeBodyCoords_H

#include "Body.h"

#include <map>
#include <memory>

namespace Simulator {

struct Vector2D;

// A class used to store the positions and velocities of a body over time.
class BodyPositionsAndVelocities {

public:
  BodyPositionsAndVelocities(std::unique_ptr<Body> body);
  ~BodyPositionsAndVelocities();

  // Removes previously calculated positions and velocities.
  void resetParameters();

  // Return the body associated with the position and velocity coordinates.
  [[nodiscard]] Body &body() const;

  // Add a mass for a specific time.
  void addMass(double const time, double const mass);
  // Add a position coordinate for a specific time.
  void addPosition(double const time, Vector2D const &position);
  // Add a velocity for a specific time.
  void addVelocity(double const time, Vector2D const &velocity);

  // Returns the bodies mass at the different times during the a simulation.
  [[nodiscard]] inline std::map<double, double> const &masses() const noexcept {
    return m_masses;
  }

  // Returns the body locations calculated during a simulation.
  [[nodiscard]] inline std::map<double, Vector2D> const &
  positions() const noexcept {
    return m_positions;
  }

  // Returns the body velocities calculated during a simulation.
  [[nodiscard]] inline std::map<double, Vector2D> const &
  velocities() const noexcept {
    return m_velocities;
  }

private:
  std::unique_ptr<Body> m_body;
  std::map<double, double> m_masses;
  std::map<double, Vector2D> m_positions;
  std::map<double, Vector2D> m_velocities;
};

} // namespace Simulator

#endif // SpaceTimeBodyCoords_H
