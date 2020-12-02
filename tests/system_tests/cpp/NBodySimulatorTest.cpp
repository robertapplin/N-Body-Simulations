// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "NBodySimulator.h"
#include "Vector2D.h"

#include "gtest/gtest.h"

#include <memory>

using namespace Simulator;

class NBodySimulatorTest : public testing::Test {
protected:
  void SetUp() override { m_simulator = std::make_unique<NBodySimulator>(); }

  void assertEqualVectors(Vector2D const &vector1, Vector2D const &vector2,
                          double tolerance = 1e-10) {
    EXPECT_NEAR(vector1.m_x, vector2.m_x, tolerance);
    EXPECT_NEAR(vector1.m_y, vector2.m_y, tolerance);
  }

  std::unique_ptr<NBodySimulator> m_simulator;
};

TEST_F(
    NBodySimulatorTest,
    test_that_a_one_body_simulation_with_a_stationary_body_returns_the_expected_body_positions) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Sun", 1.0, {1.0, 2.0}, {0.0, 0.0});

  ASSERT_NO_THROW(m_simulator->runSimulation());

  auto const sunPosition = m_simulator->simulatedPositions("Sun");

  assertEqualVectors({1.0, 2.0}, sunPosition.at(0.0));
  assertEqualVectors({1.0, 2.0}, sunPosition.at(1.0));
  assertEqualVectors({1.0, 2.0}, sunPosition.at(2.0));

  assertEqualVectors({1.0, 2.0}, sunPosition.at(498.0));
  assertEqualVectors({1.0, 2.0}, sunPosition.at(499.0));
  assertEqualVectors({1.0, 2.0}, sunPosition.at(500.0));
}

TEST_F(
    NBodySimulatorTest,
    test_that_a_one_body_simulation_with_a_moving_body_returns_the_expected_body_positions) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Sun", 1.0, {1.0, 2.0}, {1.0, 1.0});

  ASSERT_NO_THROW(m_simulator->runSimulation());

  auto const sunPosition = m_simulator->simulatedPositions("Sun");

  assertEqualVectors({1.0, 2.0}, sunPosition.at(0.0));
  assertEqualVectors({2.0, 3.0}, sunPosition.at(1.0));
  assertEqualVectors({3.0, 4.0}, sunPosition.at(2.0));

  assertEqualVectors({499.0, 500.0}, sunPosition.at(498.0));
  assertEqualVectors({500.0, 501.0}, sunPosition.at(499.0));
  assertEqualVectors({501.0, 502.0}, sunPosition.at(500.0));
}

TEST_F(NBodySimulatorTest,
       test_that_a_two_body_simulation_returns_the_expected_body_positions) {
  m_simulator->setTimeStep(1.0);
  m_simulator->setDuration(500.0);
  m_simulator->addBody("Sun", 1.0, {0.0, 0.0}, {0.0, 0.0});
  m_simulator->addBody("Earth", 0.000003, {1.0, 0.0}, {0.0, 0.015});

  ASSERT_NO_THROW(m_simulator->runSimulation());

  auto const sunPosition = m_simulator->simulatedPositions("Sun");

  assertEqualVectors({0.0000000000, 0.0000000000}, sunPosition.at(0.0));
  assertEqualVectors({0.0000000009, 0.0000000000}, sunPosition.at(1.0));
  assertEqualVectors({0.0000000027, 0.0000000000}, sunPosition.at(2.0));
  assertEqualVectors({0.0000000053, 0.0000000000}, sunPosition.at(3.0));
  assertEqualVectors({0.0000000089, 0.0000000001}, sunPosition.at(4.0));

  assertEqualVectors({0.0000004755, 0.0000237419}, sunPosition.at(496.0));
  assertEqualVectors({0.0000004473, 0.0000237492}, sunPosition.at(497.0));
  assertEqualVectors({0.0000004200, 0.0000237562}, sunPosition.at(498.0));
  assertEqualVectors({0.0000003935, 0.0000237627}, sunPosition.at(499.0));
  assertEqualVectors({0.0000003679, 0.0000237687}, sunPosition.at(500.0));

  auto const earthPosition = m_simulator->simulatedPositions("Earth");

  assertEqualVectors({1.0000000000, 0.0000000000}, earthPosition.at(0.0));
  assertEqualVectors({0.9997040894, 0.0149999999}, earthPosition.at(1.0));
  assertEqualVectors({0.9991121928, 0.0299955589}, earthPosition.at(2.0));
  assertEqualVectors({0.9982242599, 0.0449822301}, earthPosition.at(3.0));
  assertEqualVectors({0.9970402648, 0.0599555601}, earthPosition.at(4.0));

  assertEqualVectors({0.8415090939, -0.4739573920}, earthPosition.at(496.0));
  assertEqualVectors({0.8508936079, -0.4614181317}, earthPosition.at(497.0));
  assertEqualVectors({0.8600004944, -0.4487283131}, earthPosition.at(498.0));
  assertEqualVectors({0.8688285829, -0.4358930165}, earthPosition.at(499.0));
  assertEqualVectors({0.8773767570, -0.4229172785}, earthPosition.at(500.0));
}
