// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/Body.h"

namespace Simulator {

Body::Body(std::string const &name, double mass,
           Vector2D const &initialPosition, Vector2D const &initialVelocity)
    : m_name(name), m_mass(mass), m_initialPosition(initialPosition),
      m_initialVelocity(initialVelocity), m_position(initialPosition),
      m_velocity(initialVelocity) {}

std::string Body::name() const { return m_name; }

void Body::setMass(double mass) { m_mass = mass; }

double Body::mass() const { return m_mass; }

Vector2D &Body::initialPosition() { return m_initialPosition; }

Vector2D &Body::initialVelocity() { return m_initialVelocity; }

Vector2D &Body::position() { return m_position; }

Vector2D &Body::velocity() { return m_velocity; }

bool Body::operator!=(Body const &otherBody) {
  return m_name != otherBody.name();
}

} // namespace Simulator
