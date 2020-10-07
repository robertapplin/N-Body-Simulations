// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef SpaceTimeBodyCoords_H
#define SpaceTimeBodyCoords_H

#include "Body.h"
#include "Vector2D.h"

#include <memory>
#include <vector>

namespace Simulator {

// A class used to store a spacial coordinate for a given time.
class SpaceTimeCoord {

public:
  SpaceTimeCoord(double time, Vector2D const &position);
  ~SpaceTimeCoord() = default;

  // Returns the stored position.
  Vector2D &position();

private:
  double m_time;
  Vector2D m_position;
};

// A class used to store the positions of a body over a period of time.
class SpaceTimeBodyCoords {

public:
  SpaceTimeBodyCoords(std::unique_ptr<Body> body, double time,
                      Vector2D const &position);
  ~SpaceTimeBodyCoords();

  // Removes the positions calculated during previous simulations.
  void resetCoords();

  // Return the body associated with the position coordinates.
  Body &body() const;

  // Add a position coordinate for a specific time.
  void addPosition(double time, Vector2D const &position);

  // Returns the body locations calculated during a simulation.
  std::vector<Vector2D> simulatedPositions() const;

private:
  std::unique_ptr<Body> m_body;
  std::vector<std::unique_ptr<SpaceTimeCoord>> m_spaceTimeCoords;
};

} // namespace Simulator

#endif // SpaceTimeBodyCoords_H
