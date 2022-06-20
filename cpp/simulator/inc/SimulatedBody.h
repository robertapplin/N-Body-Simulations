// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#pragma once

#include "Body.h"
#include "BodyEvolution.h"

#include <memory>

namespace Simulator {

struct Vector2D;

// A class used to store data about a Body in a simulation.
class SimulatedBody {
public:
  SimulatedBody(std::unique_ptr<Body> body,
                std::unique_ptr<BodyEvolution> bodyEvolution);

  ~SimulatedBody();

  // Returns the body associated with the simulated body.
  [[nodiscard]] Body &body();
  // Returns the evolutions of the body over time.
  [[nodiscard]] BodyEvolution &bodyEvolution();

  // Returns the name of the body.
  [[nodiscard]] std::string const &name() const;

  // Add a mass, position and velocity for a specific time.
  void addTime(double const time, double const mass, Vector2D const position,
               Vector2D const velocity);

  // Resets the body and its time evolution.
  void reset();

private:
  // The body associated with this simulated body.
  std::unique_ptr<Body> m_body;
  // The evolutions in the bodies mass, position and velocity over time.
  std::unique_ptr<BodyEvolution> m_bodyEvolution;
};

} // namespace Simulator
