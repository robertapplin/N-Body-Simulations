// Project Repository : https://github.com/robertapplin/N-Body-Simulations
// Authored by Robert Applin, 2020
#include "Vector2D.h"

#include "gtest/gtest.h"

using namespace Simulator;

class Vector2DTest : public testing::Test {
protected:
  void SetUp() override {
    m_vector1 = {3.0, 4.0};
    m_vector2 = {1.0, 2.0};
  }

  Vector2D m_vector1;
  Vector2D m_vector2;
};

TEST_F(Vector2DTest, test_that_magnitude_returns_the_magnitude_of_the_vector) {
  ASSERT_EQ(5.0, m_vector1.magnitude());
}

TEST_F(
    Vector2DTest,
    test_that_the_equal_to_operator_will_return_true_when_the_vectors_are_equal) {
  ASSERT_TRUE(m_vector1 == m_vector1);
}

TEST_F(
    Vector2DTest,
    test_that_the_equal_to_operator_will_return_false_when_the_vectors_are_not_equal) {
  ASSERT_FALSE(m_vector1 == m_vector2);
}

TEST_F(Vector2DTest,
       test_that_the_subtract_operator_will_subtract_two_vectors) {
  ASSERT_TRUE(Vector2D({2.0, 2.0}) == m_vector1 - m_vector2);
}

TEST_F(
    Vector2DTest,
    test_that_the_multiply_operator_will_multiply_a_vector_by_a_given_number) {
  ASSERT_TRUE(Vector2D({15.0, 20.0}) == m_vector1 * 5);
}

TEST_F(Vector2DTest,
       test_that_the_plus_equals_operator_will_add_onto_a_vector) {
  m_vector1 += {2.0, 2.0};
  ASSERT_TRUE(Vector2D({5.0, 6.0}) == m_vector1);
}
