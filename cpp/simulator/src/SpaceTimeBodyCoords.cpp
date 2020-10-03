// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/SpaceTimeBodyCoords.h"

namespace simulator {

SpaceTimeCoord::SpaceTimeCoord(double time, double x, double y, double vx,
                               double vy)
    : m_time(time), m_position({x, y}), m_velocity({x, y}) {}

Vector2D SpaceTimeCoord::position() const { return m_position; }

Vector2D SpaceTimeCoord::velocity() const { return m_velocity; }

SpaceTimeBodyCoords::SpaceTimeBodyCoords(std::shared_ptr<Body> const &body)
    : m_body(body), m_spaceTimeCoords() {}

} // namespace simulator
