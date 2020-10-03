// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef NBodySimulator_H
#define NBodySimulator_H

#include "Body.h"
#include "SpaceTimeBodyCoords.h"

#include <memory>
#include <string>
#include <vector>

namespace simulator {

class NBodySimulator {

public:
  NBodySimulator();

  void setName(std::string const &name);
  std::string getName() const;

private:
  std::string m_name;
  std::vector<std::shared_ptr<Body>> m_bodies;
  std::vector<std::unique_ptr<SpaceTimeBodyCoords>> m_bodyCoords;
};

} // namespace simulator

#endif
