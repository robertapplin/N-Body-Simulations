// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "BodyPositionsAndVelocities.h"

#include "Vector2D.h"

#include <stdexcept>

namespace Simulator {

BodyPositionsAndVelocities::BodyPositionsAndVelocities(
    std::unique_ptr<Body> body)
    : m_body(std::move(body)), m_positions(), m_velocities() {
  m_positions[0.0] = m_body->initialPosition();
  m_velocities[0.0] = m_body->initialVelocity();
}

BodyPositionsAndVelocities::~BodyPositionsAndVelocities() {
  m_body.reset();
  m_positions.clear();
  m_velocities.clear();
}

void BodyPositionsAndVelocities::resetParameters() {
  m_positions.erase(std::next(m_positions.cbegin()), m_positions.cend());
  m_velocities.erase(std::next(m_velocities.cbegin()), m_velocities.cend());
  m_body->resetBody();
}

Body &BodyPositionsAndVelocities::body() const { return *m_body.get(); }

void BodyPositionsAndVelocities::addPosition(double time,
                                             Vector2D const &position) {
  if (m_positions.find(time) != m_positions.cend())
    throw std::runtime_error("A position for " + m_body->name() + " at time " +
                             std::to_string(time) + " already exists.");

  m_positions[time] = position;
}

void BodyPositionsAndVelocities::addVelocity(double time,
                                             Vector2D const &velocity) {
  if (m_velocities.find(time) != m_velocities.cend())
    throw std::runtime_error("A velocity for " + m_body->name() + " at time " +
                             std::to_string(time) + " already exists.");

  m_velocities[time] = velocity;
}

} // namespace Simulator
