// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "NBodySimulator.h"

#include "Body.h"
#include "SimulationConstants.h"
#include "Vector2D.h"

#include <algorithm>
#include <cmath>
#include <iterator>
#include <numeric>
#include <stdexcept>

namespace {

auto const getName = [](auto const &data) -> std::string {
  return data->body().name();
};

auto const hasNameLambda(std::string const &name) {
  auto const hasName = [&name](auto const &data) -> bool {
    return data->body().name() == name;
  };
  return hasName;
}

auto const resetParameters = [](auto const &data) -> void { data->reset(); };

void mergeBodies(Simulator::Body &targetBody, Simulator::Body &otherBody) {
  targetBody.setMass(targetBody.mass() + otherBody.mass());
  otherBody.setAsMerged(true);

  auto &velocity = targetBody.velocity();
  velocity += otherBody.velocity() * (otherBody.mass() / targetBody.mass());
};

Simulator::Vector2D const
calculateAccelerationFromOtherBody(Simulator::Body &targetBody,
                                   Simulator::Body &otherBody,
                                   double const gravitationalConstant) {
  auto const relativePosition = otherBody.position() - targetBody.position();
  auto const r = relativePosition.magnitude();
  auto const collision = r <= targetBody.radius() + otherBody.radius();

  if (collision && targetBody.mass() >= otherBody.mass()) {
    mergeBodies(targetBody, otherBody);
    return Simulator::Vector2D{0.0, 0.0};
  } else {
    return relativePosition *
           (gravitationalConstant * otherBody.mass() / pow(r, 3));
  }
};

void accumulateAccelerationFromOtherBody(Simulator::Vector2D &acceleration,
                                         Simulator::Body &targetBody,
                                         Simulator::Body &otherBody,
                                         double const gravitationalConstant) {
  if (!otherBody.isMerged() && targetBody != otherBody) {
    acceleration += calculateAccelerationFromOtherBody(targetBody, otherBody,
                                                       gravitationalConstant);
  }
}

} // namespace

namespace Simulator {
using namespace Constants;

NBodySimulator::NBodySimulator()
    : m_timeStep(0.0), m_duration(0.0),
      m_gravitationalConstant(gravitationalConstant(TimeUnit::Days)),
      m_bodyData(), m_dataChanged(true) {}

NBodySimulator::~NBodySimulator() { clear(); }

void NBodySimulator::clear() {
  m_timeStep = 0.0;
  m_duration = 0.0;
  m_bodyData.clear();
  m_dataChanged = true;
}

void NBodySimulator::removeBody(std::string const &name) {
  m_dataChanged = std::erase_if(m_bodyData, hasNameLambda(name)) != 0u;

  if (!m_dataChanged) {
    throw std::invalid_argument("The body '" + name + "' could not be found.");
  }
}

void NBodySimulator::addBody(std::string const &name, double const mass,
                             Vector2D const &position,
                             Vector2D const &velocity) {
  if (std::get<0>(hasBody(name)))
    throw std::invalid_argument("The body '" + name + "' already exists.");

  m_bodyData.emplace_back(std::make_unique<BodyEvolution>(
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
  if (std::get<0>(hasBody(newName)))
    throw std::invalid_argument("The body '" + newName + "' already exists.");

  getBody(oldName).setName(newName);
  m_dataChanged = true;
}

void NBodySimulator::setMass(std::string const &bodyName, double const mass) {
  getBody(bodyName).setInitialMass(mass);
  m_dataChanged = true;
}

double const NBodySimulator::initialMass(std::string const &bodyName) const {
  return getBody(bodyName).initialMass();
}

void NBodySimulator::setXPosition(std::string const &bodyName, double const x) {
  getBody(bodyName).initialPosition().m_x = x;
  m_dataChanged = true;
}

void NBodySimulator::setYPosition(std::string const &bodyName, double const y) {
  getBody(bodyName).initialPosition().m_y = y;
  m_dataChanged = true;
}

void NBodySimulator::setXVelocity(std::string const &bodyName,
                                  double const vx) {
  getBody(bodyName).initialVelocity().m_x = vx;
  m_dataChanged = true;
}

void NBodySimulator::setYVelocity(std::string const &bodyName,
                                  double const vy) {
  getBody(bodyName).initialVelocity().m_y = vy;
  m_dataChanged = true;
}

Vector2D const
NBodySimulator::initialPosition(std::string const &bodyName) const {
  return getBody(bodyName).initialPosition();
}

Vector2D const
NBodySimulator::initialVelocity(std::string const &bodyName) const {
  return getBody(bodyName).initialVelocity();
}

bool const NBodySimulator::hasDataChanged() const { return m_dataChanged; }

void NBodySimulator::runSimulation() {
  validateSimulationParameters();

  if (m_dataChanged) {
    resetSimulation();
    for (auto const steps = timeSteps(); auto const &i : steps) {
      calculateNewPositions(i);
    }
    m_dataChanged = false;
  }
}

std::map<double, BodyState> const
NBodySimulator::simulationResults(std::string const &bodyName) const {
  auto const bodyIndex = findBodyIndex(bodyName);
  return m_bodyData[bodyIndex]->timeEvolutions();
}

void NBodySimulator::validateSimulationParameters() const {
  if (m_bodyData.empty()) {
    throw std::invalid_argument("There are no bodies in the simulation.");
  } else if (m_timeStep <= 0.0) {
    throw std::invalid_argument("The time step must be above zero.");
  } else if (m_duration <= 0.0) {
    throw std::invalid_argument("The duration must be above zero.");
  } else if (m_timeStep > m_duration) {
    throw std::invalid_argument(
        "The time step cannot be larger than the duration.");
  } else if (std::fmod(static_cast<int>(m_duration * 10.0),
                       static_cast<int>(m_timeStep * 10.0)) != 0.0) {
    throw std::invalid_argument(
        "The duration must be evenly divisible by the time step.");
  }
}

void NBodySimulator::calculateNewPositions(std::size_t const &stepNumber) {

  auto const calculateNewPosition = [&](auto const &data) -> void {
    auto &targetBody = data->body();
    if (!targetBody.isMerged()) {
      auto const targetBodyIndex = findBodyIndex(targetBody.name());
      calculateNewPositionForBody(stepNumber, targetBodyIndex, targetBody);
    }
  };

  std::for_each(m_bodyData.begin(), m_bodyData.end(), calculateNewPosition);
}

void NBodySimulator::calculateNewPositionForBody(
    std::size_t const &stepNumber, std::size_t const &targetBodyIndex,
    Body &targetBody) {
  auto const acceleration = calculateAcceleration(targetBody);

  auto &velocity = targetBody.velocity();
  velocity += acceleration * m_timeStep;

  auto &position = targetBody.position();
  position += velocity * m_timeStep;

  auto const time = stepNumber * m_timeStep;
  m_bodyData[targetBodyIndex]->addTime(time, targetBody.mass(), position,
                                       velocity);
}

Vector2D NBodySimulator::calculateAcceleration(Body &targetBody) {
  Vector2D acceleration = {0.0, 0.0};

  auto const accumulateAcceleration = [&](auto const &data) -> void {
    auto &otherBody = data->body();
    accumulateAccelerationFromOtherBody(acceleration, targetBody, otherBody,
                                        m_gravitationalConstant);
  };

  std::for_each(m_bodyData.begin(), m_bodyData.end(), accumulateAcceleration);
  return acceleration;
}

void NBodySimulator::resetSimulation() {
  std::for_each(m_bodyData.begin(), m_bodyData.end(), resetParameters);
}

std::size_t const NBodySimulator::numberOfSteps() const {
  return static_cast<std::size_t const>(std::llround(m_duration / m_timeStep));
}

std::vector<std::size_t> const NBodySimulator::timeSteps() const {
  std::vector<std::size_t> timeSteps;
  timeSteps.reserve(numberOfSteps());
  std::iota(timeSteps.begin(), timeSteps.end(), 1u);
  return timeSteps;
}

Body &NBodySimulator::getBody(std::string const &name) const {
  return getBody(findBodyIndex(name));
}

Body &NBodySimulator::getBody(std::size_t const &bodyIndex) const {
  if (bodyIndex < numberOfBodies()) {
    return m_bodyData[bodyIndex]->body();
  }

  throw std::invalid_argument("The body index " + std::to_string(bodyIndex) +
                              " is too large.");
}

std::size_t const NBodySimulator::findBodyIndex(std::string const &name) const {
  auto const [exists, iter] = hasBody(name);
  if (exists)
    return std::distance(m_bodyData.cbegin(), iter);

  throw std::invalid_argument("The body '" + name + "' could not be found.");
}

std::tuple<bool const, BodyData::const_iterator> const
NBodySimulator::hasBody(std::string const &name) const {
  auto const iter =
      std::find_if(m_bodyData.cbegin(), m_bodyData.cend(), hasNameLambda(name));
  return {iter != m_bodyData.cend(), iter};
}

} // namespace Simulator
