// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/SpaceTimeBodyCoords.h"

namespace Simulator {

// Methods for the SpaceTimeCoord class.
SpaceTimeCoord::SpaceTimeCoord(double time, Vector2D const &position)
    : m_time(time), m_position(position) {}

Vector2D &SpaceTimeCoord::position() { return m_position; }

// Methods for the SpaceTimeBodyCoords class.
SpaceTimeBodyCoords::SpaceTimeBodyCoords(std::unique_ptr<Body> body,
                                         double time, Vector2D const &position)
    : m_body(std::move(body)), m_spaceTimeCoords() {
  m_spaceTimeCoords = std::vector<std::unique_ptr<SpaceTimeCoord>>();
  m_spaceTimeCoords.emplace_back(
      std::make_unique<SpaceTimeCoord>(time, position));
}

SpaceTimeBodyCoords::~SpaceTimeBodyCoords() {
  m_body.reset();
  m_spaceTimeCoords.clear();
}

void SpaceTimeBodyCoords::resetCoords() {
  m_spaceTimeCoords.resize(1);
  m_body->resetBody();
}

Body &SpaceTimeBodyCoords::body() const { return *m_body.get(); }

void SpaceTimeBodyCoords::addPosition(double time, Vector2D const &position) {
  m_spaceTimeCoords.emplace_back(
      std::make_unique<SpaceTimeCoord>(time, position));
}

std::vector<Vector2D> SpaceTimeBodyCoords::simulatedPositions() const {
  std::vector<Vector2D> positions;
  positions.reserve(m_spaceTimeCoords.size());

  for (auto const &coord : m_spaceTimeCoords)
    positions.emplace_back(coord->position());
  return positions;
}

} // namespace Simulator
