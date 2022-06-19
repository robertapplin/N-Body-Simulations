// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "BodyEvolution.h"
#include "Vector2D.h"

#include "gtest/gtest.h"

#include <memory>
#include <stdexcept>

using namespace Simulator;

class BodyPositionsTest : public testing::Test {
protected:
  void SetUp() override {
    m_bodyPositions = std::make_unique<BodyEvolution>(std::make_unique<Body>(
        "Earth", 0.01, Vector2D({1.0, 2.0}), Vector2D({3.0, 4.0})));
  }

  std::unique_ptr<BodyEvolution> m_bodyPositions;
};

TEST_F(BodyPositionsTest,
       test_that_BodyPositions_has_been_instantiated_with_the_correct_body) {
  ASSERT_EQ("Earth", m_bodyPositions->body().name());
  ASSERT_EQ(0.01, m_bodyPositions->body().initialMass());
}

TEST_F(
    BodyPositionsTest,
    test_that_BodyPositions_has_been_instantiated_with_a_single_position_and_velocity_at_time_zero) {
  auto const results = m_bodyPositions->timeEvolutions();

  ASSERT_EQ(1, results.size());
  ASSERT_EQ(0.01, std::get<0>(results.at(0.0)));
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == std::get<1>(results.at(0.0)));
  ASSERT_TRUE(Vector2D({3.0, 4.0}) == std::get<2>(results.at(0.0)));
}

TEST_F(BodyPositionsTest, test_that_addTime_will_add_data_for_a_time) {
  m_bodyPositions->addTime(1.0, 2.0, Vector2D({5.0, 6.0}),
                           Vector2D({7.0, 8.0}));

  auto const results = m_bodyPositions->timeEvolutions();

  ASSERT_EQ(2, results.size());
  ASSERT_EQ(2.0, std::get<0>(results.at(1.0)));
  ASSERT_TRUE(Vector2D({5.0, 6.0}) == std::get<1>(results.at(1.0)));
  ASSERT_TRUE(Vector2D({7.0, 8.0}) == std::get<2>(results.at(1.0)));
}

TEST_F(BodyPositionsTest,
       test_that_addTime_will_throw_when_a_time_already_exists) {
  ASSERT_THROW(m_bodyPositions->addTime(0.0, 2.0, Vector2D({5.0, 6.0}),
                                        Vector2D({7.0, 8.0})),
               std::runtime_error);
}

TEST_F(BodyPositionsTest,
       test_that_reset_will_clear_all_positions_and_velocities_but_the_first) {
  m_bodyPositions->addTime(1.0, 2.0, Vector2D({3.0, 3.0}),
                           Vector2D({4.0, 4.0}));

  m_bodyPositions->reset();

  auto const results = m_bodyPositions->timeEvolutions();
  ASSERT_EQ(1, results.size());
  ASSERT_EQ(0.01, std::get<0>(results.at(0.0)));
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == std::get<1>(results.at(0.0)));
  ASSERT_TRUE(Vector2D({3.0, 4.0}) == std::get<2>(results.at(0.0)));
}

TEST_F(
    BodyPositionsTest,
    test_that_reset_will_reset_the_positions_and_velocities_in_the_body_back_to_the_initial_values) {
  auto &position = m_bodyPositions->body().position();
  position += {3.0, 3.0};
  auto &velocity = m_bodyPositions->body().velocity();
  velocity += {3.0, 3.0};

  m_bodyPositions->addTime(1.0, 2.0, position, velocity);

  m_bodyPositions->reset();

  auto const results = m_bodyPositions->timeEvolutions();
  ASSERT_EQ(1, results.size());
  ASSERT_TRUE(Vector2D({1.0, 2.0}) == std::get<1>(results.at(0.0)));
  ASSERT_TRUE(Vector2D({3.0, 4.0}) == std::get<2>(results.at(0.0)));
}
