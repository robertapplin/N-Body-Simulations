// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef Body_H
#define Body_H

#include "Vector2D.h"

#include <string>

namespace Simulator {

class Body {

public:
  Body(std::string const &name, double mass, Vector2D const &initialPosition,
       Vector2D const &initialVelocity);
  ~Body() = default;

  std::string name() const;

  void setMass(double mass);
  double mass() const;

  Vector2D &initialPosition();
  Vector2D &initialVelocity();

  Vector2D &position();
  Vector2D &velocity();

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

#endif
