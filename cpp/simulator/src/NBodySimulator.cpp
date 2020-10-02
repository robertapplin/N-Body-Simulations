// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/NBodySimulator.h"

namespace simulator {

NBodySimulator::NBodySimulator(std::string const &name) { m_name = name; }

std::string NBodySimulator::getName() const { return m_name; }

} // namespace simulator
