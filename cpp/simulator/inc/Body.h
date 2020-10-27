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
  std::string name() const;

  // Sets the mass of the body.
  void setMass(double mass);
  // Returns the mass of the body.
  double mass() const;

  // Returns the initial position of the body.
  Vector2D &initialPosition();
  // Returns the initial velocity of the body.
  Vector2D &initialVelocity();

  // Returns the current position of the body.
  Vector2D &position();
  // Returns the current velocity of the body.
  Vector2D &velocity();

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
