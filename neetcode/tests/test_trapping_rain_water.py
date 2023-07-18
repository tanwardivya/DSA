from unittest import TestCase
from two_pointer.trapping_rain_water import Solution
class TestSolution(TestCase):
    def test_trapping_rain_water_1(self):
        solution = Solution()
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        expected_result = 6
        actual_result = solution.trapping_rain_water(height)
        self.assertEqual(actual_result,expected_result)

    def test_trapping_rain_water_2(self):
        solution = Solution()
        height = [4,2,0,3,2,5]
        expected_result = 9
        actual_result = solution.trapping_rain_water(height)
        self.assertEqual(actual_result,expected_result)
