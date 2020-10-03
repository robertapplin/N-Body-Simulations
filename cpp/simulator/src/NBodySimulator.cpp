// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/NBodySimulator.h"

namespace simulator {

NBodySimulator::NBodySimulator() : m_bodyNames(), m_bodyCoords() {}

void NBodySimulator::addBody(std::string const &name, double mass,
                             Vector2D const &position,
                             Vector2D const &velocity) {
  auto const body = std::make_shared<Body>(name, mass);
  m_bodyNames.emplace_back(body);
  m_bodyCoords.emplace_back(std::make_unique<SpaceTimeBodyCoords>(body));
}

void NBodySimulator::setName(std::string const &name) { m_name = name; }

std::string NBodySimulator::getName() const { return m_name; }

} // namespace simulator
