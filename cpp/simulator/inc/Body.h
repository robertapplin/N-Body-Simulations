// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef Body_H
#define Body_H

#include "Vector2D.h"

#include <string>

namespace Simulator {

// A class used to store data about a Body in a simulation.
class Body {

public:
  Body(std::string const &name, double mass, Vector2D const &initialPosition,
       Vector2D const &initialVelocity);
  ~Body() = default;

  // Sets the name of the body.
  void setName(std::string const &name);
  // Returns the name of the body.
  inline std::string name() const noexcept { return m_name; }

  // Sets the mass of the body.
  void setMass(double mass);
  // Returns the mass of the body.
  inline double mass() const noexcept { return m_mass; }

  // Returns the initial position of the body.
  inline Vector2D &initialPosition() noexcept { return m_initialPosition; }
  // Returns the initial velocity of the body.
  inline Vector2D &initialVelocity() noexcept { return m_initialVelocity; }

  // Returns the current position of the body.
  inline Vector2D &position() noexcept { return m_position; }
  // Returns the current velocity of the body.
  inline Vector2D &velocity() noexcept { return m_velocity; }

  // Reset the position and velocity of the body to the initial values.
  void resetBody();

  bool operator!=(Body const &otherBody);

private:
  std::string m_name;
  double m_mass;

  Vector2D m_initialPosition;
  Vector2D m_initialVelocity;

  Vector2D m_position;
  Vector2D m_velocity;
};

} // namespace Simulator

#endif // Body_H
