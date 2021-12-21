// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#ifndef Body_H
#define Body_H

#include "Vector2D.h"

#include <string>

namespace Simulator {

// A class used to store data about a Body in a simulation.
class Body {

public:
  Body(std::string name, const double initialMass, Vector2D initialPosition,
       Vector2D initialVelocity);
  ~Body() = default;

  // Sets the name of the body.
  void setName(std::string const &name);
  // Returns the name of the body.
  [[nodiscard]] inline std::string name() const noexcept { return m_name; }

  // Sets the initial mass of the body.
  void setInitialMass(double const mass);
  // Returns the mass of the body.
  [[nodiscard]] inline double initialMass() const noexcept {
    return m_initialMass;
  }

  // Sets the current mass of the body.
  void setMass(double const mass);
  // Returns the current mass of the body.
  [[nodiscard]] inline double mass() const noexcept { return m_mass; }

  // Returns the initial position of the body.
  [[nodiscard]] inline Vector2D &initialPosition() noexcept {
    return m_initialPosition;
  }
  // Returns the initial velocity of the body.
  [[nodiscard]] inline Vector2D &initialVelocity() noexcept {
    return m_initialVelocity;
  }

  // Returns the current position of the body.
  [[nodiscard]] inline Vector2D &position() noexcept { return m_position; }
  // Returns the current velocity of the body.
  [[nodiscard]] inline Vector2D &velocity() noexcept { return m_velocity; }

  // Returns an estimated radius for the body.
  [[nodiscard]] double radius() const;

  // Reset the position and velocity of the body to the initial values.
  void resetBody();

  // Sets the body as having been engulfed by a larger body.
  void setAsMerged(bool const merged);
  // Returns true if this body has merged into a larger body.
  [[nodiscard]] inline bool isMerged() const noexcept { return m_isMerged; }

  bool operator!=(Body const &otherBody);

private:
  std::string m_name;
  double m_initialMass;

  Vector2D m_initialPosition;
  Vector2D m_initialVelocity;

  double m_mass;

  Vector2D m_position;
  Vector2D m_velocity;

  bool m_isMerged;
};

} // namespace Simulator

#endif // Body_H
