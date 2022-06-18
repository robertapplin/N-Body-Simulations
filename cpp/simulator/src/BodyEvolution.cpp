// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "BodyEvolution.h"

#include "Vector2D.h"

#include <stdexcept>

namespace Simulator {

BodyEvolution::BodyEvolution(std::unique_ptr<Body> body)
    : m_body(std::move(body)), m_evolutions() {
  m_evolutions[0.0] = {m_body->initialMass(), m_body->initialPosition(),
                       m_body->initialVelocity()};
}

BodyEvolution::~BodyEvolution() {
  m_body.reset();
  m_evolutions.clear();
}

void BodyEvolution::resetParameters() {
  m_evolutions.erase(std::next(m_evolutions.cbegin()), m_evolutions.cend());
  m_body->resetBody();
}

Body &BodyEvolution::body() const { return *m_body.get(); }

void BodyEvolution::addTime(double const time, double const mass,
                            Vector2D const position, Vector2D const velocity) {
  if (m_evolutions.find(time) != m_evolutions.cend()) {
    throw std::runtime_error("Data for " + m_body->name() + " at time " +
                             std::to_string(time) + " already exists.");
  }

  m_evolutions[time] = {mass, position, velocity};
}

} // namespace Simulator
