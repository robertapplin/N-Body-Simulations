// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "SpaceTimeBodyCoords.h"

namespace Simulator {

BodyPositions::BodyPositions(std::unique_ptr<Body> body, double time,
                             Vector2D const &position)
    : m_body(std::move(body)), m_positions() {
  m_positions[time] = position;
}

BodyPositions::~BodyPositions() {
  m_body.reset();
  m_positions.clear();
}

void BodyPositions::resetCoords() {
  m_positions.erase(std::next(m_positions.begin()), m_positions.end());
  m_body->resetBody();
}

Body &BodyPositions::body() const { return *m_body.get(); }

void BodyPositions::addPosition(double time, Vector2D const &position) {
  if (m_positions.find(time) != m_positions.end())
    throw std::runtime_error("A position for " + m_body->name() + " at time " +
                             std::to_string(time) + " already exists.");

  m_positions[time] = position;
}

std::map<double, Vector2D> BodyPositions::positions() const {
  return m_positions;
}

} // namespace Simulator
