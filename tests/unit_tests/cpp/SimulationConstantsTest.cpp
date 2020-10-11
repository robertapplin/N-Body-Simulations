// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "SimulationConstants.h"

#include "gtest/gtest.h"

using namespace Simulator::Constants;

TEST(SimulationConstantsTest,
     test_that_the_gravitional_constant_is_correct_when_the_time_unit_is_days) {
  EXPECT_NEAR(0.000295911, gravitationalConstant(TimeUnit::Days), 1e-9);
}
