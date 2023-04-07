// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "NBodySimulator.h"

#include "Body.h"
#include "SimulationConstants.h"
#include "Vector2D.h"

#include <algorithm>
#include <cmath>
#include <iterator>
#include <stdexcept>

namespace {

auto const getName = [](auto const &data) { return data->body().name(); };

auto const hasNameLambda(std::string const &name) {
  return [&name](auto const &data) { return data->body().name() == name; };
}

} // namespace

namespace Simulator {
using namespace Constants;

NBodySimulator::NBodySimulator()
    : m_timeStep(0.0), m_duration(0.0),
      m_gravitationalConstant(gravitationalConstant(TimeUnit::Days)),
      m_bodyData(), m_dataChanged(true) {}

NBodySimulator::~NBodySimulator() { m_bodyData.clear(); }

void NBodySimulator::clear() {
  m_timeStep = 0.0;
  m_duration = 0.0;
  m_bodyData.clear();
  m_dataChanged = true;
}

void NBodySimulator::removeBody(std::string const &name) {
  if (std::erase_if(m_bodyData, hasNameLambda(name)) != 0u) {
    m_dataChanged = true;
  } else {
    throw std::invalid_argument("The body '" + name + "' could not be found.");
  }
}

void NBodySimulator::addBody(std::string const &name, double const mass,
                             Vector2D const &position,
                             Vector2D const &velocity) {
  if (hasBody(name))
    throw std::invalid_argument("The body '" + name + "' already exists.");

  m_bodyData.emplace_back(std::make_unique<BodyPositionsAndVelocities>(
      std::make_unique<Body>(name, mass, position, velocity)));
  m_dataChanged = true;
}

void NBodySimulator::setTimeStep(double const timeStep) {
  m_timeStep = timeStep;
  m_dataChanged = true;
}

double const NBodySimulator::timeStep() const { return m_timeStep; }

void NBodySimulator::setDuration(double const duration) {
  m_duration = duration;
  m_dataChanged = true;
}

double const NBodySimulator::duration() const { return m_duration; }

std::size_t const NBodySimulator::numberOfBodies() const {
  return m_bodyData.size();
}

std::vector<std::string> const NBodySimulator::bodyNames() const {
  std::vector<std::string> names;
  names.reserve(numberOfBodies());
  std::transform(m_bodyData.cbegin(), m_bodyData.cend(),
                 std::back_inserter(names), getName);
  return names;
}

void NBodySimulator::setName(std::string const &oldName,
                             std::string const &newName) {
  if (hasBody(newName))
    throw std::invalid_argument("The body '" + newName + "' already exists.");

  findBody(oldName).setName(newName);
  m_dataChanged = true;
}

void NBodySimulator::setMass(std::string const &bodyName, double const mass) {
  auto &body = findBody(bodyName);
  body.setInitialMass(mass);
  body.setMass(mass);
  m_dataChanged = true;
}

double const NBodySimulator::initialMass(std::string const &bodyName) const {
  return findBody(bodyName).initialMass();
}

void NBodySimulator::setXPosition(std::string const &bodyName, double const x) {
  findBody(bodyName).initialPosition().m_x = x;
  m_dataChanged = true;
}

void NBodySimulator::setYPosition(std::string const &bodyName, double const y) {
  findBody(bodyName).initialPosition().m_y = y;
  m_dataChanged = true;
}

void NBodySimulator::setXVelocity(std::string const &bodyName,
                                  double const vx) {
  findBody(bodyName).initialVelocity().m_x = vx;
  m_dataChanged = true;
}

void NBodySimulator::setYVelocity(std::string const &bodyName,
                                  double const vy) {
  findBody(bodyName).initialVelocity().m_y = vy;
  m_dataChanged = true;
}

Vector2D const
NBodySimulator::initialPosition(std::string const &bodyName) const {
  return findBody(bodyName).initialPosition();
}

Vector2D const
NBodySimulator::initialVelocity(std::string const &bodyName) const {
  return findBody(bodyName).initialVelocity();
}

bool const NBodySimulator::hasDataChanged() const { return m_dataChanged; }

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

std::map<double, double> const
NBodySimulator::simulatedMasses(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->masses();
}

std::map<double, Vector2D> const
NBodySimulator::simulatedPositions(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->positions();
}

std::map<double, Vector2D> const
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
  else if (std::fmod(static_cast<int>(m_duration * 10.0),
                     static_cast<int>(m_timeStep * 10.0)) != 0.0)
    throw std::invalid_argument(
        "The duration must be evenly divisible by the time step.");
}

void NBodySimulator::calculateNewPositions(std::size_t const &stepNumber) {
  for (auto const &targetBodyName : bodyNames()) {
    auto const targetBodyIndex = findBodyIndex(targetBodyName);
    if (!body(targetBodyIndex).isMerged()) {
      calculateNewPositions(stepNumber, targetBodyIndex, body(targetBodyIndex));
    }
  }
}

void NBodySimulator::calculateNewPositions(std::size_t const &stepNumber,
                                           std::size_t const &targetBodyIndex,
                                           Body &targetBody) {
  auto acceleration = calculateAcceleration(targetBody);

  auto &velocity = targetBody.velocity();
  velocity += acceleration * m_timeStep;

  auto &position = targetBody.position();
  position += velocity * m_timeStep;

  auto const time = stepNumber * m_timeStep;
  m_bodyData[targetBodyIndex]->addMass(time, targetBody.mass());
  m_bodyData[targetBodyIndex]->addPosition(time, position);
  m_bodyData[targetBodyIndex]->addVelocity(time, velocity);
}

Vector2D NBodySimulator::calculateAcceleration(Body &targetBody) {
  Vector2D acceleration = {0.0, 0.0};

  for (auto const &data : m_bodyData)
    if (!data->body().isMerged())
      calculateAcceleration(acceleration, targetBody, data->body());
  return acceleration;
}

void NBodySimulator::calculateAcceleration(Vector2D &acceleration,
                                           Body &targetBody, Body &otherBody) {
  if (targetBody != otherBody) {
    auto relativePosition = otherBody.position() - targetBody.position();
    auto const r = relativePosition.magnitude();
    auto const collision = r <= targetBody.radius() + otherBody.radius();
    if (collision && targetBody.mass() >= otherBody.mass()) {
      mergeBodies(targetBody, otherBody);
    } else {
      acceleration += relativePosition *
                      (m_gravitationalConstant * otherBody.mass() / pow(r, 3));
    }
  }
}

void NBodySimulator::mergeBodies(Body &largerBody, Body &smallerBody) {
  largerBody.setMass(largerBody.mass() + smallerBody.mass());
  smallerBody.setAsMerged(true);

  auto &velocity = largerBody.velocity();
  velocity += smallerBody.velocity() * (smallerBody.mass() / largerBody.mass());
}

Body &NBodySimulator::body(std::size_t const &bodyIndex) {
  return m_bodyData[bodyIndex]->body();
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
  auto const iter = std::find(names.cbegin(), names.cend(), name);
  return iter != names.cend();
}

Body &NBodySimulator::findBody(std::string const &name) const {
  return m_bodyData[findBodyIndex(name)]->body();
}

std::size_t const NBodySimulator::findBodyIndex(std::string const &name) const {
  auto const iter =
      std::find_if(m_bodyData.cbegin(), m_bodyData.cend(), hasNameLambda(name));
  if (iter != m_bodyData.cend())
    return std::distance(m_bodyData.cbegin(), iter);

  throw std::invalid_argument("The body '" + name + "' could not be found.");
}

} // namespace Simulator
