// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/SpaceTimeBodyCoords.h"

namespace simulator {

SpaceTimeCoord::SpaceTimeCoord(double time, double x, double y, double vx,
                               double vy)
    : m_time(time), m_position({x, y}), m_velocity({x, y}) {}

SpaceTimeCoord::SpaceTimeCoord(double time, Vector2D const &position,
                               Vector2D const &velocity)
    : m_time(time), m_position(position), m_velocity(velocity) {}

Vector2D &SpaceTimeCoord::position() { return m_position; }

Vector2D &SpaceTimeCoord::velocity() { return m_velocity; }

SpaceTimeBodyCoords::SpaceTimeBodyCoords(std::unique_ptr<Body> body,
                                         double time, Vector2D const &position,
                                         Vector2D const &velocity)
    : m_body(std::move(body)), m_spaceTimeCoords() {
  m_spaceTimeCoords = std::vector<std::unique_ptr<SpaceTimeCoord>>();
  m_spaceTimeCoords.emplace_back(
      std::make_unique<SpaceTimeCoord>(time, position, velocity));
}

SpaceTimeBodyCoords::~SpaceTimeBodyCoords() {
  m_body.reset();
  m_spaceTimeCoords.clear();
}

Body &SpaceTimeBodyCoords::body() const { return *m_body.get(); }

Vector2D &SpaceTimeBodyCoords::initialPosition() const {
  if (m_spaceTimeCoords.size() > 0)
    return m_spaceTimeCoords[0]->position();

  throw std::runtime_error("An initial position for " + m_body->name() +
                           " could not be found.");
}

Vector2D &SpaceTimeBodyCoords::initialVelocity() const {
  if (m_spaceTimeCoords.size() > 0)
    return m_spaceTimeCoords[0]->velocity();

  throw std::runtime_error("An initial velocity for " + m_body->name() +
                           " could not be found.");
}

} // namespace simulator
