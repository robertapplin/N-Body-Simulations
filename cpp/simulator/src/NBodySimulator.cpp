// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/NBodySimulator.h"

#include <algorithm>

namespace simulator {

NBodySimulator::NBodySimulator()
    : m_timeStep(1.0), m_duration(500.0), m_bodyData() {}

void NBodySimulator::removeBody(std::string const &name) {
  auto const bodyIndex = findBodyIndex(name);
  m_bodyData.erase(m_bodyData.begin() + bodyIndex);
}

void NBodySimulator::addBody(std::string const &name, double mass,
                             Vector2D const &position,
                             Vector2D const &velocity) {
  m_bodyData.emplace_back(std::make_unique<SpaceTimeBodyCoords>(
      std::make_unique<Body>(name, mass), 0.0, position, velocity));
}

void NBodySimulator::setTimeStep(double timeStep) { m_timeStep = timeStep; }

double NBodySimulator::timeStep() const { return m_timeStep; }

void NBodySimulator::setDuration(double duration) { m_duration = duration; }

double NBodySimulator::duration() const { return m_duration; }

std::size_t NBodySimulator::numberOfBodies() const { return m_bodyData.size(); }

std::vector<std::string> NBodySimulator::bodyNames() const {
  std::vector<std::string> names;
  names.reserve(numberOfBodies());

  for (auto const &data : m_bodyData)
    names.emplace_back(data->body().name());
  return names;
}

void NBodySimulator::setMass(std::string const &bodyName, double mass) {
  auto const bodyIndex = findBodyIndex(bodyName);
  m_bodyData[bodyIndex]->body().setMass(mass);
}

double NBodySimulator::mass(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->body().mass();
}

void NBodySimulator::setXPosition(std::string const &bodyName, double x) {
  auto const bodyIndex = findBodyIndex(bodyName);
  m_bodyData[bodyIndex]->initialPosition().m_x = x;
}

void NBodySimulator::setYPosition(std::string const &bodyName, double y) {
  auto const bodyIndex = findBodyIndex(bodyName);
  m_bodyData[bodyIndex]->initialPosition().m_y = y;
}

void NBodySimulator::setXVelocity(std::string const &bodyName, double vx) {
  auto const bodyIndex = findBodyIndex(bodyName);
  m_bodyData[bodyIndex]->initialVelocity().m_x = vx;
}

void NBodySimulator::setYVelocity(std::string const &bodyName, double vy) {
  auto const bodyIndex = findBodyIndex(bodyName);
  m_bodyData[bodyIndex]->initialVelocity().m_y = vy;
}

Vector2D NBodySimulator::initialPosition(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->initialPosition();
}

Vector2D NBodySimulator::initialVelocity(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->initialVelocity();
}

std::size_t NBodySimulator::findBodyIndex(std::string const &name) const {
  auto const hasName = [&](std::unique_ptr<SpaceTimeBodyCoords> const &coords) {
    return coords->body().name() == name;
  };

  auto const iter = std::find_if(m_bodyData.begin(), m_bodyData.end(), hasName);
  if (iter != m_bodyData.end())
    return iter - m_bodyData.begin();

  throw std::runtime_error("The body '" + name + "' could not be found.");
}

} // namespace simulator
