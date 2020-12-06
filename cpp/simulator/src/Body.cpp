// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "Body.h"
#include "SimulationConstants.h"

#include <cmath>

#define _USE_MATH_DEFINES
#include <math.h>

namespace Simulator {

Body::Body(std::string const &name, double initialMass,
           Vector2D const &initialPosition, Vector2D const &initialVelocity)
    : m_name(name), m_initialMass(initialMass),
      m_initialPosition(initialPosition), m_initialVelocity(initialVelocity),
      m_mass(initialMass), m_position(initialPosition),
      m_velocity(initialVelocity), m_isMerged(false) {}

void Body::setName(std::string const &name) { m_name = name; }

void Body::setInitialMass(double mass) { m_initialMass = mass; }

void Body::setMass(double mass) { m_mass = mass; }

double Body::radius() const {
  return pow((3.0 * m_mass) / (4.0 * M_PI * Constants::density(m_mass)),
             (1.0 / 3.0));
}

void Body::resetBody() {
  m_mass = m_initialMass;
  m_position = m_initialPosition;
  m_velocity = m_initialVelocity;
  m_isMerged = false;
}

void Body::setAsMerged(bool merged) { m_isMerged = merged; }

bool Body::operator!=(Body const &otherBody) {
  return m_name != otherBody.name();
}

} // namespace Simulator
