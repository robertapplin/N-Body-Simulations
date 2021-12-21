// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "Body.h"
#include "SimulationConstants.h"

#include <cmath>

#define _USE_MATH_DEFINES
#include <math.h>

namespace Simulator {

Body::Body(std::string name, double const initialMass, Vector2D initialPosition,
           Vector2D initialVelocity)
    : m_name(std::move(name)), m_initialMass(initialMass),
      m_initialPosition(std::move(initialPosition)),
      m_initialVelocity(std::move(initialVelocity)), m_mass(initialMass),
      m_position(initialPosition), m_velocity(initialVelocity),
      m_isMerged(false) {}

void Body::setName(std::string const &name) { m_name = name; }

void Body::setInitialMass(double const mass) {
  m_initialMass = mass;
  m_mass = mass;
}

void Body::setMass(double const mass) { m_mass = mass; }

double const Body::radius() const {
  return pow((3.0 * m_mass) / (4.0 * M_PI * Constants::density(m_mass)),
             (1.0 / 3.0));
}

void Body::resetBody() {
  m_mass = m_initialMass;
  m_position = m_initialPosition;
  m_velocity = m_initialVelocity;
  m_isMerged = false;
}

void Body::setAsMerged(bool const merged) { m_isMerged = merged; }

bool const Body::operator!=(Body const &otherBody) {
  return m_name != otherBody.name();
}

} // namespace Simulator
