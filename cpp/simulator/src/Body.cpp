// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/Body.h"

namespace simulator {

Body::Body(std::string const &name, double mass) : m_name(name), m_mass(mass) {}

std::string Body::name() const { return m_name; }

double Body::mass() const { return m_mass; }

} // namespace simulator
