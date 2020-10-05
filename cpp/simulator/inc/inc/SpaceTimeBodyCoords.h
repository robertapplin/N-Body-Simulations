// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef SpaceTimeBodyCoords_H
#define SpaceTimeBodyCoords_H

#include "Body.h"
#include "Vector2D.h"

#include <memory>
#include <vector>

namespace Simulator {

class SpaceTimeCoord {

public:
  SpaceTimeCoord(double time, Vector2D const &position);
  ~SpaceTimeCoord() = default;

  Vector2D &position();

private:
  double m_time;
  Vector2D m_position;
};

class SpaceTimeBodyCoords {

public:
  SpaceTimeBodyCoords(std::unique_ptr<Body> body, double time,
                      Vector2D const &position);
  ~SpaceTimeBodyCoords();

  void resetCoords();

  Body &body() const;

  void addPosition(double time, Vector2D const &position);

  std::vector<Vector2D> simulatedPositions() const;

private:
  std::unique_ptr<Body> m_body;
  std::vector<std::unique_ptr<SpaceTimeCoord>> m_spaceTimeCoords;
};

} // namespace Simulator

#endif // SpaceTimeBodyCoords_H
