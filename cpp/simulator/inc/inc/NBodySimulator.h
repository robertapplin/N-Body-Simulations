#ifndef NBodySimulator_H
#define NBodySimulator_H

#include <string>

namespace simulator {

class NBodySimulator {

public:
  NBodySimulator(std::string const &name);

  std::string getName() const;

private:
  std::string m_name;
};

} // namespace simulator

#endif
