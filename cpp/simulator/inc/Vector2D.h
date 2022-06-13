// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef Vector2D_H
#define Vector2D_H

namespace Simulator {

// A struct used for two dimensional vector operations.
struct Vector2D {
  // Calculates the magnitude of the two dimensional vector.
  [[nodiscard]] double const magnitude() const;

  // Used to simplify vector operations.
  Vector2D const operator-(Vector2D const &otherVector) const;
  Vector2D const operator*(double const value) const;
  void operator+=(Vector2D const &otherVector);
  bool const operator==(Vector2D const &otherVector) const;

  double m_x;
  double m_y;
};

} // namespace Simulator

#endif // Vector2D_H
