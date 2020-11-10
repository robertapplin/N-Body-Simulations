// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef NBodySimulator_H
#define NBodySimulator_H

#include "BodyPositions.h"

#include <map>
#include <memory>
#include <string>
#include <vector>

namespace Simulator {

class Body;
struct Vector2D;

// A class which can be used to simulate an N-Body system.
class NBodySimulator {

public:
  NBodySimulator();
  ~NBodySimulator();

  // Removes the body with the specified name from the simulator.
  void removeBody(std::string const &name);
  // Adds a body to the simulator.
  void addBody(std::string const &name, double mass, Vector2D const &position,
               Vector2D const &velocity);

  // Set the time step used by the simulator.
  void setTimeStep(double timeStep);
  // Return the time step stored by the simulator.
  double timeStep() const;

  // Set the simulation duration used by the simulator.
  void setDuration(double duration);
  // Return the simulation duration stored by the simulator.
  double duration() const;

  // Return the number of bodies in the simulation setup.
  std::size_t numberOfBodies() const;

  // Returns the names of the bodies in the simulator.
  std::vector<std::string> bodyNames() const;

  // Set a new name for the specified body in the simulator.
  void setName(std::string const &oldName, std::string const &newName);

  // Set the mass of the specified body in the simulator.
  void setMass(std::string const &bodyName, double mass);
  // Return the mass of the specified body stored by the simulator.
  double mass(std::string const &bodyName) const;

  // Set the x position of the specified body in the simulator.
  void setXPosition(std::string const &bodyName, double x);
  // Set the y position of the specified body in the simulator.
  void setYPosition(std::string const &bodyName, double y);

  // Set the x velocity of the specified body in the simulator.
  void setXVelocity(std::string const &bodyName, double vx);
  // Set the y velocity of the specified body in the simulator.
  void setYVelocity(std::string const &bodyName, double vy);

  // Return the initial position of the specified body stored by the simulator.
  Vector2D initialPosition(std::string const &bodyName) const;
  // Return the initial velocity of the specified body stored by the simulator.
  Vector2D initialVelocity(std::string const &bodyName) const;

  // Returns true if the initial parameters changed since the last simulation.
  bool hasDataChanged() const;

  // Run the simulation using the currently stored initial parameters.
  void runSimulation();

  // Return the simulated locations of the specified body.
  std::map<double, Vector2D>
  simulatedPositions(std::string const &bodyName) const;

private:
  // Checks that the provided parameters are valid, and throws if they are not.
  void validateSimulationParameters() const;

  // Calculates the new positions of the bodies at the next time step.
  void calculateNewPositions(std::size_t const &stepNumber);
  // Calculates the new positions of a target body at the next time step.
  void calculateNewPositions(std::size_t const &stepNumber,
                             std::size_t const &bodyIndex, Body &targetBody);
  // Calculates the accelerations of the bodies at the next time step.
  Vector2D calculateAcceleration(Body &targetBody) const;
  // Calculates the acceleration of a target body at the next time step.
  void calculateAcceleration(Vector2D &acceleration, Body &targetBody,
                             Body &otherBody) const;

  // Removes the data calculated during previous simulations.
  void resetSimulation();

  // Returns the number of steps to take in the simulation.
  std::size_t numberOfSteps() const;

  // Returns true if the simulator contains a body with the given name.
  bool hasBody(std::string const &name) const;

  // Finds the Body data object given a bodies name.
  Body &findBody(std::string const &name) const;
  // Finds the index of the specified body in m_bodyData.
  std::size_t findBodyIndex(std::string const &name) const;

  double m_timeStep;
  double m_duration;
  double m_gravitationalConstant;

  // The vector containing each body and their simulated positions.
  std::vector<std::unique_ptr<BodyPositions>> m_bodyData;
  // A flag to notify when the data changes in-between simulations.
  bool m_dataChanged;
};

} // namespace Simulator

#endif // NBodySimulator_H
