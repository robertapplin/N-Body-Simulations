// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "../inc/inc/Vector2D.h"

#include <cmath>

namespace simulator {

double Vector2D::magnitude() const {
  return pow(pow(m_x, 2) + pow(m_y, 2), 0.5);
}

Vector2D Vector2D::operator-(Vector2D const &otherVector) {
  return {m_x - otherVector.m_x, m_y - otherVector.m_y};
}

Vector2D Vector2D::operator*(double value) {
  return {m_x * value, m_y * value};
}

void Vector2D::operator+=(Vector2D const &otherVector) {
  m_x += otherVector.m_x;
  m_y += otherVector.m_y;
}

bool Vector2D::operator==(Vector2D const &otherVector) {
  return m_x == otherVector.m_x && m_y == otherVector.m_y;
}

} // namespace simulator
