// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "Body.h"
#include "Vector2D.h"

#include "gtest/gtest.h"

#include <memory>

using namespace Simulator;

class BodyTest : public testing::Test {
protected:
  void SetUp() override {
    m_body = std::make_unique<Body>("Earth", 0.01, Vector2D({1.0, 2.0}),
                                    Vector2D({3.0, 4.0}));
  }

  std::unique_ptr<Body> m_body;
};

TEST_F(BodyTest, test_that_name_returns_the_name_of_the_body) {
  ASSERT_EQ("Earth", m_body->name());
}

TEST_F(BodyTest, test_that_setName_will_set_the_name_of_the_body) {
  m_body->setName("Sun");
  ASSERT_EQ("Sun", m_body->name());
}

TEST_F(BodyTest, test_that_mass_returns_the_mass_of_the_body) {
  ASSERT_EQ(0.01, m_body->initialMass());
  ASSERT_EQ(0.01, m_body->mass());
}

TEST_F(BodyTest, test_that_setMass_will_set_the_mass_of_the_body) {
  m_body->setInitialMass(5.0);
  ASSERT_EQ(5.0, m_body->initialMass());
  ASSERT_EQ(5.0, m_body->mass());
}

TEST_F(BodyTest,
       test_that_initialPosition_will_return_the_initial_position_of_the_body) {
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == m_body->initialPosition());
}

TEST_F(BodyTest,
       test_that_initialVelocity_will_return_the_initial_velocity_of_the_body) {
  ASSERT_TRUE(Vector2D({3.0, 4.0}) == m_body->initialVelocity());
}

TEST_F(
    BodyTest,
    test_that_position_will_return_the_initial_position_when_no_other_positions_exist) {
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == m_body->position());
}

TEST_F(
    BodyTest,
    test_that_velocity_will_return_the_initial_velocity_when_no_other_velocities_exist) {
  ASSERT_TRUE(Vector2D({3.0, 4.0}) == m_body->velocity());
}

TEST_F(BodyTest, test_that_the_current_position_of_the_body_can_be_set) {
  m_body->position() += {2.0, 2.0};
  ASSERT_TRUE(Vector2D({3.0, 4.0}) == m_body->position());
}

TEST_F(BodyTest, test_that_the_current_velocity_of_the_body_can_be_set) {
  m_body->velocity() += {2.0, 2.0};
  ASSERT_TRUE(Vector2D({5.0, 6.0}) == m_body->velocity());
}

TEST_F(BodyTest, test_that_the_body_is_not_merged_by_default) {
  ASSERT_TRUE(!m_body->isMerged());
}

TEST_F(BodyTest, test_that_setAsMerged_will_set_the_body_as_being_merged) {
  m_body->setAsMerged(true);
  ASSERT_TRUE(m_body->isMerged());
}

TEST_F(
    BodyTest,
    test_that_resetBody_will_reset_the_current_position_and_velocity_of_the_body) {
  m_body->position() += {2.0, 2.0};
  m_body->velocity() += {2.0, 2.0};
  m_body->setAsMerged(true);

  m_body->resetBody();

  ASSERT_TRUE(Vector2D({1.0, 2.0}) == m_body->position());
  ASSERT_TRUE(Vector2D({3.0, 4.0}) == m_body->velocity());
  ASSERT_TRUE(!m_body->isMerged());
}

TEST_F(BodyTest,
       test_the_not_equal_to_operator_returns_false_when_the_bodies_are_equal) {
  ASSERT_FALSE(m_body.get() != m_body.get());
}

TEST_F(
    BodyTest,
    test_the_not_equal_to_operator_returns_true_when_the_bodies_are_not_equal) {
  auto const otherBody = std::make_unique<Body>(
      "Sun", 1.0, Vector2D({0.0, 0.0}), Vector2D({0.0, 0.0}));
  ASSERT_TRUE(otherBody.get() != m_body.get());
}
