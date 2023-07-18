from unittest import TestCase
from two_pointer.container_with_most_water import Solution
class TestSolution(TestCase):
    def test_container_with_most_water_1(self):
        solution = Solution()
        height = [1,8,6,2,5,4,8,3,7]
        expected_result = 49
        actual_result = solution.container_with_most_water(height)
        self.assertEqual(actual_result,expected_result)

    def test_container_with_most_water_2(self):
        solution = Solution()
        height = [1,1]
        expected_result = 1
        actual_result = solution.container_with_most_water(height)
        self.assertEqual(actual_result,expected_result)