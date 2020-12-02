// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "NBodySimulator.h"
#include "Vector2D.h"

#include "gtest/gtest.h"

#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

using namespace Simulator;

class NBodySimulatorTest : public testing::Test {
protected:
  void SetUp() override {
    m_simulator = std::make_unique<NBodySimulator>();
    m_simulator->addBody("Sun", 1.0, {0.0, 0.0}, {0.0, 0.0});
  }

  std::unique_ptr<NBodySimulator> m_simulator;
};

TEST_F(
    NBodySimulatorTest,
    test_that_numberOfBodies_will_return_the_number_of_bodies_in_the_simulator) {
  ASSERT_EQ(1, m_simulator->numberOfBodies());
}

TEST_F(
    NBodySimulatorTest,
    test_that_removeBody_will_remove_the_body_without_throwing_if_it_exists) {
  ASSERT_NO_THROW(m_simulator->removeBody("Sun"));
  ASSERT_EQ(0, m_simulator->numberOfBodies());
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_removeBody_will_throw_if_the_body_does_not_exist) {
  ASSERT_THROW(m_simulator->removeBody("Earth"), std::invalid_argument);
  ASSERT_EQ(1, m_simulator->numberOfBodies());
}

TEST_F(NBodySimulatorTest,
       test_that_addBody_will_throw_if_the_body_already_exists) {
  ASSERT_THROW(m_simulator->addBody("Sun", 1.0, {0.0, 0.0}, {0.0, 0.0}),
               std::invalid_argument);
  ASSERT_EQ(1, m_simulator->numberOfBodies());
}

TEST_F(NBodySimulatorTest,
       test_that_addBody_will_not_throw_if_the_body_does_not_exist) {
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});
  ASSERT_EQ(2, m_simulator->numberOfBodies());
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest, test_that_setTimeStep_will_change_the_time_step) {
  m_simulator->setTimeStep(5.0);
  ASSERT_EQ(5.0, m_simulator->timeStep());
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_setDuration_will_change_the_simulation_duration) {
  m_simulator->setDuration(600.0);
  ASSERT_EQ(600.0, m_simulator->duration());
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(
    NBodySimulatorTest,
    test_that_bodyNames_will_return_the_names_of_the_bodies_help_by_the_simulator) {
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});

  auto const bodyNames = m_simulator->bodyNames();

  auto const expectedNames = std::vector<std::string>({"Sun", "Earth"});
  ASSERT_EQ(2, bodyNames.size());
  ASSERT_EQ(expectedNames, bodyNames);
}

TEST_F(NBodySimulatorTest, test_that_setName_will_set_the_name_of_a_body) {
  m_simulator->setName("Sun", "Jupiter");

  auto const expectedNames = std::vector<std::string>({"Jupiter"});
  ASSERT_EQ(expectedNames, m_simulator->bodyNames());
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_setName_will_throw_if_the_old_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->setName("Neptune", "Jupiter"),
               std::invalid_argument);
}

TEST_F(NBodySimulatorTest, test_that_setMass_will_set_the_mass_of_a_body) {
  m_simulator->setMass("Sun", 2.0);
  ASSERT_EQ(2.0, m_simulator->mass("Sun"));
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_setMass_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->setMass("Neptune", 2.0), std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_mass_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->mass("Neptune"), std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_setXPosition_will_set_the_initial_x_position_of_a_body) {
  m_simulator->setXPosition("Sun", 2.0);
  ASSERT_EQ(2.0, m_simulator->initialPosition("Sun").m_x);
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_setXPosition_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->setXPosition("Neptune", 2.0),
               std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_setYPosition_will_set_the_initial_y_position_of_a_body) {
  m_simulator->setYPosition("Sun", 2.0);
  ASSERT_EQ(2.0, m_simulator->initialPosition("Sun").m_y);
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_setYPosition_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->setYPosition("Neptune", 2.0),
               std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_setXVelocity_will_set_the_initial_x_velocity_of_a_body) {
  m_simulator->setXVelocity("Sun", 2.0);
  ASSERT_EQ(2.0, m_simulator->initialVelocity("Sun").m_x);
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_setXVelocity_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->setXVelocity("Neptune", 2.0),
               std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_setYVelocity_will_set_the_initial_y_position_of_a_body) {
  m_simulator->setYVelocity("Sun", 2.0);
  ASSERT_EQ(2.0, m_simulator->initialVelocity("Sun").m_y);
  ASSERT_TRUE(m_simulator->hasDataChanged());
}

TEST_F(NBodySimulatorTest,
       test_that_setYVelocity_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->setYVelocity("Neptune", 2.0),
               std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_initialPosition_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->initialPosition("Neptune"), std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_initialVelocity_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->initialVelocity("Neptune"), std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_runSimulation_will_not_throw_if_the_data_is_all_correct) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});
  ASSERT_NO_THROW(m_simulator->runSimulation());
}

TEST_F(
    NBodySimulatorTest,
    test_that_runSimulation_will_throw_if_two_bodies_have_the_same_position) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Earth", 0.000003, {0.0, 0.0}, {0.0, 0.015});
  ASSERT_THROW(m_simulator->runSimulation(), std::runtime_error);
}

TEST_F(NBodySimulatorTest,
       test_that_runSimulation_will_throw_if_no_bodies_are_in_the_simulation) {
  m_simulator->removeBody("Sun");
  ASSERT_THROW(m_simulator->runSimulation(), std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_runSimulation_will_throw_if_the_time_step_is_zero) {
  m_simulator->setTimeStep(0.0);
  ASSERT_THROW(m_simulator->runSimulation(), std::invalid_argument);
}

TEST_F(NBodySimulatorTest,
       test_that_runSimulation_will_throw_if_the_duration_is_zero) {
  m_simulator->setDuration(0.0);
  ASSERT_THROW(m_simulator->runSimulation(), std::invalid_argument);
}

TEST_F(
    NBodySimulatorTest,
    test_that_runSimulation_will_throw_if_the_time_step_is_larger_than_the_duration) {
  m_simulator->setTimeStep(10.0);
  m_simulator->setDuration(5.0);
  ASSERT_THROW(m_simulator->runSimulation(), std::invalid_argument);
}

TEST_F(
    NBodySimulatorTest,
    test_that_runSimulation_will_throw_if_the_duration_is_not_divisible_by_the_time_step) {
  m_simulator->setTimeStep(1.3);
  m_simulator->setDuration(20.0);
  ASSERT_THROW(m_simulator->runSimulation(), std::invalid_argument);
}

TEST_F(
    NBodySimulatorTest,
    test_that_simulatedPositions_will_return_a_map_of_positions_with_the_correct_size) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});

  m_simulator->runSimulation();

  auto sunPositions = m_simulator->simulatedPositions("Sun");
  auto earthPositions = m_simulator->simulatedPositions("Earth");

  ASSERT_EQ(501, sunPositions.size());
  ASSERT_EQ(501, earthPositions.size());
}

TEST_F(
    NBodySimulatorTest,
    test_that_simulatedPositions_will_return_the_initial_positions_in_a_map) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});

  m_simulator->runSimulation();

  auto const sunPositions = m_simulator->simulatedPositions("Sun");
  auto const earthPositions = m_simulator->simulatedPositions("Earth");

  ASSERT_TRUE(Vector2D({0.0, 0.0}) == sunPositions.at(0.0));
  ASSERT_TRUE(Vector2D({1.0, 0.0}) == earthPositions.at(0.0));
}

TEST_F(
    NBodySimulatorTest,
    test_that_simulatedPositions_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->simulatedPositions("Earth"), std::invalid_argument);
}

TEST_F(
    NBodySimulatorTest,
    test_that_simulatedVelocities_will_return_a_map_of_velocities_with_the_correct_size) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});

  m_simulator->runSimulation();

  auto sunVelocities = m_simulator->simulatedVelocities("Sun");
  auto earthVelocities = m_simulator->simulatedVelocities("Earth");

  ASSERT_EQ(501, sunVelocities.size());
  ASSERT_EQ(501, earthVelocities.size());
}

TEST_F(
    NBodySimulatorTest,
    test_that_simulatedVelocities_will_return_the_initial_positions_in_a_map) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});

  m_simulator->runSimulation();

  auto const sunVelocities = m_simulator->simulatedVelocities("Sun");
  auto const earthVelocities = m_simulator->simulatedVelocities("Earth");

  ASSERT_TRUE(Vector2D({0.0, 0.0}) == sunVelocities.at(0.0));
  ASSERT_TRUE(Vector2D({0.0, 0.015}) == earthVelocities.at(0.0));
}

TEST_F(
    NBodySimulatorTest,
    test_that_simulatedVelocities_will_throw_if_the_body_name_does_not_exist) {
  ASSERT_THROW(m_simulator->simulatedVelocities("Earth"),
               std::invalid_argument);
}
