// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "Body.h"

namespace Simulator {

Body::Body(std::string const &name, double mass,
           Vector2D const &initialPosition, Vector2D const &initialVelocity)
    : m_name(name), m_mass(mass), m_initialPosition(initialPosition),
      m_initialVelocity(initialVelocity), m_position(initialPosition),
      m_velocity(initialVelocity) {}

void Body::setName(std::string const &name) { m_name = name; }

void Body::setMass(double mass) { m_mass = mass; }

void Body::resetBody() {
  m_position = m_initialPosition;
  m_velocity = m_initialVelocity;
}

bool Body::operator!=(Body const &otherBody) {
  return m_name != otherBody.name();
}

} // namespace Simulator
