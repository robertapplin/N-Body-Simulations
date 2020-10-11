// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef SpaceTimeBodyCoords_H
#define SpaceTimeBodyCoords_H

#include "Body.h"
#include "Vector2D.h"

#include <map>
#include <memory>

namespace Simulator {

// A class used to store the positions of a body over a period of time.
class BodyPositions {

public:
  BodyPositions(std::unique_ptr<Body> body);
  ~BodyPositions();

  // Removes the positions calculated during previous simulations.
  void resetPositions();

  // Return the body associated with the position coordinates.
  Body &body() const;

  // Add a position coordinate for a specific time.
  void addPosition(double time, Vector2D const &position);

  // Returns the body locations calculated during a simulation.
  std::map<double, Vector2D> positions() const;

private:
  std::unique_ptr<Body> m_body;
  std::map<double, Vector2D> m_positions;
};

} // namespace Simulator

#endif // SpaceTimeBodyCoords_H
