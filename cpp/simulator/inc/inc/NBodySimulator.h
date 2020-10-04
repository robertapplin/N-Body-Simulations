// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef NBodySimulator_H
#define NBodySimulator_H

#include "Body.h"
#include "SpaceTimeBodyCoords.h"
#include "Vector2D.h"

#include <memory>
#include <string>
#include <vector>

namespace simulator {

class NBodySimulator {

public:
  NBodySimulator();

  void removeBody(std::string const &name);
  void addBody(std::string const &name, double mass, Vector2D const &position,
               Vector2D const &velocity);

  void setTimeStep(double timeStep);
  double timeStep() const;

  void setDuration(double duration);
  double duration() const;

  std::size_t numberOfBodies() const;

  std::vector<std::string> bodyNames() const;

  void setMass(std::string const &bodyName, double mass);
  double mass(std::string const &bodyName) const;

  void setXPosition(std::string const &bodyName, double x);
  void setYPosition(std::string const &bodyName, double y);

  void setXVelocity(std::string const &bodyName, double vx);
  void setYVelocity(std::string const &bodyName, double vy);

  Vector2D initialPosition(std::string const &bodyName) const;
  Vector2D initialVelocity(std::string const &bodyName) const;

  bool hasDataChanged() const;

  bool runSimulation();

private:
  void resetSimulation();

  bool hasBody(std::string const &name) const;

  std::size_t findBodyIndex(std::string const &name) const;

  double m_timeStep;
  double m_duration;
  std::vector<std::unique_ptr<SpaceTimeBodyCoords>> m_bodyData;
  // Has the initial data changed since the last simulation
  bool m_dataChanged;
};

} // namespace simulator

#endif
