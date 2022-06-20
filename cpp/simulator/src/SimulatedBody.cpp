// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "SimulatedBody.h"

#include "Vector2D.h"

namespace Simulator {

SimulatedBody::SimulatedBody(std::unique_ptr<Body> body,
                             std::unique_ptr<BodyEvolution> bodyEvolution)
    : m_body(std::move(body)), m_bodyEvolution(std::move(bodyEvolution)) {}

SimulatedBody::~SimulatedBody() {
  m_body.reset();
  m_bodyEvolution.reset();
}

Body &SimulatedBody::body() { return *m_body.get(); }

BodyEvolution &SimulatedBody::bodyEvolution() { return *m_bodyEvolution.get(); }

std::string const &SimulatedBody::name() const { return m_body->name(); }

void SimulatedBody::addTime(double const time, double const mass,
                            Vector2D const position, Vector2D const velocity) {
  m_bodyEvolution->addTime(time, mass, position, velocity);
}

void SimulatedBody::reset() {
  m_body->reset();
  m_bodyEvolution->reset();
}

} // namespace Simulator
