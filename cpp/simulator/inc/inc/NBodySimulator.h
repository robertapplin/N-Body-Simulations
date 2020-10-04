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

  void addBody(std::string const &name, double mass, Vector2D const &position,
               Vector2D const &velocity);
  void removeBody(std::string const &name);

  std::size_t numberOfBodies() const;

  std::vector<std::string> bodyNames() const;

  double mass(std::string const &bodyName) const;

  Vector2D initialPosition(std::string const &bodyName) const;
  Vector2D initialVelocity(std::string const &bodyName) const;

private:
  std::size_t findBodyIndex(std::string const &name) const;

  std::vector<std::unique_ptr<SpaceTimeBodyCoords>> m_bodyData;
};

} // namespace simulator

#endif
