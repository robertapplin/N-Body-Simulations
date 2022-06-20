// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "BodyEvolution.h"

#include "Vector2D.h"

#include <stdexcept>

namespace Simulator {

BodyEvolution::BodyEvolution(double const mass, Vector2D position,
                             Vector2D velocity)
    : m_evolutions() {
  m_evolutions[0.0] = {mass, std::move(position), std::move(velocity)};
}

BodyEvolution::~BodyEvolution() { m_evolutions.clear(); }

void BodyEvolution::reset() {
  m_evolutions.erase(std::next(m_evolutions.cbegin()), m_evolutions.cend());
}

void BodyEvolution::addTime(double const time, double const mass,
                            Vector2D const position, Vector2D const velocity) {
  if (m_evolutions.find(time) != m_evolutions.cend()) {
    throw std::runtime_error("Data at time " + std::to_string(time) +
                             " already exists.");
  }

  m_evolutions[time] = {mass, position, velocity};
}

} // namespace Simulator
