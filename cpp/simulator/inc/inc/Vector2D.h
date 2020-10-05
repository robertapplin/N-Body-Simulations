// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef Vector2D_H
#define Vector2D_H

namespace simulator {

struct Vector2D {
  double m_x;
  double m_y;

  double magnitude() const;

  Vector2D operator-(Vector2D const &otherVector);
  Vector2D operator*(double value);
  void operator+=(Vector2D const &otherVector);
  bool operator==(Vector2D const &otherVector);
};

} // namespace simulator

#endif
