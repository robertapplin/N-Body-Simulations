// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "NBodySimulator.h"

#include "Body.h"
#include "SimulationConstants.h"
#include "Vector2D.h"

#include <algorithm>
#include <cmath>
#include <stdexcept>

namespace Simulator {
using namespace Constants;

NBodySimulator::NBodySimulator()
    : m_timeStep(1.0), m_duration(500.0),
      m_gravitationalConstant(gravitationalConstant(TimeUnit::Days)),
      m_bodyData(), m_dataChanged(true) {}

NBodySimulator::~NBodySimulator() { m_bodyData.clear(); }

void NBodySimulator::removeBody(std::string const &name) {
  m_bodyData.erase(m_bodyData.begin() + findBodyIndex(name));
  m_dataChanged = true;
}

void NBodySimulator::addBody(std::string const &name, double mass,
                             Vector2D const &position,
                             Vector2D const &velocity) {
  if (hasBody(name))
    throw std::invalid_argument("The body '" + name + "' already exists.");

  m_bodyData.emplace_back(std::make_unique<BodyPositionsAndVelocities>(
      std::make_unique<Body>(name, mass, position, velocity)));
  m_dataChanged = true;
}

void NBodySimulator::setTimeStep(double timeStep) {
  m_timeStep = timeStep;
  m_dataChanged = true;
}

double NBodySimulator::timeStep() const { return m_timeStep; }

void NBodySimulator::setDuration(double duration) {
  m_duration = duration;
  m_dataChanged = true;
}

double NBodySimulator::duration() const { return m_duration; }

std::size_t NBodySimulator::numberOfBodies() const { return m_bodyData.size(); }

std::vector<std::string> NBodySimulator::bodyNames() const {
  std::vector<std::string> names;
  names.reserve(numberOfBodies());

  for (auto const &data : m_bodyData)
    names.emplace_back(data->body().name());
  return names;
}

void NBodySimulator::setName(std::string const &oldName,
                             std::string const &newName) {
  if (hasBody(newName))
    throw std::invalid_argument("The body '" + newName + "' already exists.");

  findBody(oldName).setName(newName);
  m_dataChanged = true;
}

void NBodySimulator::setMass(std::string const &bodyName, double mass) {
  findBody(bodyName).setMass(mass);
  m_dataChanged = true;
}

double NBodySimulator::mass(std::string const &bodyName) const {
  return findBody(bodyName).mass();
}

void NBodySimulator::setXPosition(std::string const &bodyName, double x) {
  findBody(bodyName).initialPosition().m_x = x;
  m_dataChanged = true;
}

void NBodySimulator::setYPosition(std::string const &bodyName, double y) {
  findBody(bodyName).initialPosition().m_y = y;
  m_dataChanged = true;
}

void NBodySimulator::setXVelocity(std::string const &bodyName, double vx) {
  findBody(bodyName).initialVelocity().m_x = vx;
  m_dataChanged = true;
}

void NBodySimulator::setYVelocity(std::string const &bodyName, double vy) {
  findBody(bodyName).initialVelocity().m_y = vy;
  m_dataChanged = true;
}

Vector2D NBodySimulator::initialPosition(std::string const &bodyName) const {
  return findBody(bodyName).initialPosition();
}

Vector2D NBodySimulator::initialVelocity(std::string const &bodyName) const {
  return findBody(bodyName).initialVelocity();
}

bool NBodySimulator::hasDataChanged() const { return m_dataChanged; }

void NBodySimulator::runSimulation() {
  validateSimulationParameters();

  if (!m_dataChanged)
    return;

  m_gravitationalConstant = gravitationalConstant(TimeUnit::Days);

  resetSimulation();

  for (auto i = 1u; i <= numberOfSteps(); ++i)
    calculateNewPositions(i);

  m_dataChanged = false;
}

std::map<double, Vector2D>
NBodySimulator::simulatedPositions(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->positions();
}

std::map<double, Vector2D>
NBodySimulator::simulatedVelocities(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->velocities();
}

void NBodySimulator::validateSimulationParameters() const {
  if (bodyNames().empty())
    throw std::invalid_argument("There are no bodies in the simulation.");
  else if (m_timeStep <= 0.0)
    throw std::invalid_argument("The time step must be above zero.");
  else if (m_duration <= 0.0)
    throw std::invalid_argument("The duration must be above zero.");
  else if (m_timeStep > m_duration)
    throw std::invalid_argument(
        "The time step cannot be larger than the duration.");
  else if (std::fmod(m_duration, m_timeStep) != 0.0)
    throw std::invalid_argument(
        "The duration must be evenly divisible by the time step.");
}

void NBodySimulator::calculateNewPositions(std::size_t const &stepNumber) {

  for (auto const &targetBodyName : bodyNames())
    calculateNewPositions(stepNumber, findBodyIndex(targetBodyName),
                          findBody(targetBodyName));
}

void NBodySimulator::calculateNewPositions(std::size_t const &stepNumber,
                                           std::size_t const &bodyIndex,
                                           Body &targetBody) {
  auto acceleration = calculateAcceleration(targetBody);

  auto &velocity = targetBody.velocity();
  velocity += acceleration * m_timeStep;

  auto &position = targetBody.position();
  position += velocity * m_timeStep;

  m_bodyData[bodyIndex]->addPosition(stepNumber * m_timeStep, position);
  m_bodyData[bodyIndex]->addVelocity(stepNumber * m_timeStep, velocity);
}

Vector2D NBodySimulator::calculateAcceleration(Body &targetBody) const {
  Vector2D acceleration = {0.0, 0.0};

  for (auto const &data : m_bodyData)
    calculateAcceleration(acceleration, targetBody, data->body());
  return acceleration;
}

void NBodySimulator::calculateAcceleration(Vector2D &acceleration,
                                           Body &targetBody,
                                           Body &otherBody) const {
  if (targetBody != otherBody) {
    auto relativePosition = otherBody.position() - targetBody.position();
    auto const r = relativePosition.magnitude();
    if (r == 0.0)
      throw std::runtime_error("Cannot divide by zero: " + targetBody.name() +
                               " and " + otherBody.name() +
                               " have the same position.");

    acceleration += relativePosition *
                    (m_gravitationalConstant * otherBody.mass() / pow(r, 3));
  }
}

void NBodySimulator::resetSimulation() {
  for (auto const &data : m_bodyData)
    data->resetParameters();
}

std::size_t NBodySimulator::numberOfSteps() const {
  return static_cast<std::size_t>(std::llround(m_duration / m_timeStep));
}

bool NBodySimulator::hasBody(std::string const &name) const {
  auto const names = bodyNames();
  auto const iter = std::find(names.begin(), names.end(), name);
  return iter != names.end();
}

Body &NBodySimulator::findBody(std::string const &name) const {
  return m_bodyData[findBodyIndex(name)]->body();
}

std::size_t NBodySimulator::findBodyIndex(std::string const &name) const {
  auto const hasName =
      [&](std::unique_ptr<BodyPositionsAndVelocities> const &parameters) {
        return parameters->body().name() == name;
      };

  auto const iter = std::find_if(m_bodyData.begin(), m_bodyData.end(), hasName);
  if (iter != m_bodyData.end())
    return iter - m_bodyData.begin();

  throw std::invalid_argument("The body '" + name + "' could not be found.");
}

} // namespace Simulator
