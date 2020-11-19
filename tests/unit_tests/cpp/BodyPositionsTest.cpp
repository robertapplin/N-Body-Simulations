// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "BodyPositionsAndVelocities.h"
#include "Vector2D.h"

#include "gtest/gtest.h"

#include <memory>
#include <stdexcept>

using namespace Simulator;

class BodyPositionsTest : public testing::Test {
protected:
  void SetUp() override {
    m_bodyPositions =
        std::make_unique<BodyPositionsAndVelocities>(std::make_unique<Body>(
            "Earth", 0.01, Vector2D({1.0, 2.0}), Vector2D({3.0, 4.0})));
  }

  std::unique_ptr<BodyPositionsAndVelocities> m_bodyPositions;
};

TEST_F(BodyPositionsTest,
       test_that_BodyPositions_has_been_instantiated_with_the_correct_body) {
  ASSERT_EQ("Earth", m_bodyPositions->body().name());
  ASSERT_EQ(0.01, m_bodyPositions->body().mass());
}

TEST_F(
    BodyPositionsTest,
    test_that_BodyPositions_has_been_instantiated_with_a_single_position_at_time_zero) {
  auto const positions = m_bodyPositions->positions();

  ASSERT_EQ(1, positions.size());
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == positions.at(0.0));
}

TEST_F(BodyPositionsTest, test_that_addPosition_will_add_a_position) {
  m_bodyPositions->addPosition(1.0, {3.0, 3.0});

  auto const positions = m_bodyPositions->positions();

  ASSERT_EQ(2, positions.size());
  ASSERT_TRUE(Vector2D({3.0, 3.0}) == positions.at(1.0));
}

TEST_F(BodyPositionsTest,
       test_that_addPosition_will_throw_when_a_time_already_exists) {
  ASSERT_THROW(m_bodyPositions->addPosition(0.0, {3.0, 3.0}),
               std::runtime_error);
}

TEST_F(BodyPositionsTest,
       test_that_resetPositions_will_clear_all_positions_but_the_first) {
  m_bodyPositions->addPosition(1.0, {3.0, 3.0});

  m_bodyPositions->resetParameters();

  auto const positions = m_bodyPositions->positions();
  ASSERT_EQ(1, positions.size());
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == positions.at(0.0));
}

TEST_F(
    BodyPositionsTest,
    test_that_resetPositions_will_reset_the_positions_in_the_body_back_to_the_initial_values) {
  auto &position = m_bodyPositions->body().position();
  position += {3.0, 3.0};

  m_bodyPositions->addPosition(1.0, position);
  m_bodyPositions->resetParameters();

  auto const positions = m_bodyPositions->positions();
  ASSERT_EQ(1, positions.size());
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == positions.at(0.0));
}
