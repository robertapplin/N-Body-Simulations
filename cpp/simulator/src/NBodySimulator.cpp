#include "../inc/inc/NBodySimulator.h"

namespace simulator {

NBodySimulator::NBodySimulator(std::string const &name) { m_name = name; }

std::string NBodySimulator::getName() const { return m_name; }

} // namespace simulator
