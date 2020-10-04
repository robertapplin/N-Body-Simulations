// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef SpaceTimeBodyCoords_H
#define SpaceTimeBodyCoords_H

#include "Body.h"
#include "Vector2D.h"

#include <memory>
#include <string>
#include <vector>

namespace simulator {

class SpaceTimeCoord {

public:
  SpaceTimeCoord(double time, double x, double y, double vx, double vy);
  SpaceTimeCoord(double time, Vector2D const &position,
                 Vector2D const &velocity);
  ~SpaceTimeCoord() = default;

  Vector2D &position();
  Vector2D &velocity();

private:
  double m_time;
  Vector2D m_position;
  Vector2D m_velocity;
};

class SpaceTimeBodyCoords {

public:
  SpaceTimeBodyCoords(std::unique_ptr<Body> body, double time,
                      Vector2D const &position, Vector2D const &velocity);
  ~SpaceTimeBodyCoords();

  Body &body() const;

  Vector2D &initialPosition() const;
  Vector2D &initialVelocity() const;

private:
  std::unique_ptr<Body> m_body;
  std::vector<std::unique_ptr<SpaceTimeCoord>> m_spaceTimeCoords;
};

} // namespace simulator

#endif
