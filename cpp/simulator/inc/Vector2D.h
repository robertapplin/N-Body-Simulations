// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef Vector2D_H
#define Vector2D_H

namespace Simulator {

// A struct used for two dimensional vector operations.
struct Vector2D {
  // Calculates the magnitude of the two dimensional vector.
  [[nodiscard]] double magnitude() const;

  // Used to simplify vector operations.
  Vector2D operator-(Vector2D const &otherVector);
  Vector2D operator*(double value);
  void operator+=(Vector2D const &otherVector);
  bool operator==(Vector2D const &otherVector);

  double m_x;
  double m_y;
};

} // namespace Simulator

#endif // Vector2D_H
