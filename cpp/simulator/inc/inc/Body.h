// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef Body_H
#define Body_H

#include "Vector2D.h"

#include <string>

namespace simulator {

class Body {

public:
  Body(std::string const &name, double mass);
  ~Body() = default;

  std::string name() const;

  void setMass(double mass);
  double mass() const;

private:
  std::string m_name;
  double m_mass;
};

} // namespace simulator

#endif
