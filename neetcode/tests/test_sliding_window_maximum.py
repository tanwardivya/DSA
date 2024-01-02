from unittest import TestCase
from sliding_window.sliding_window_maximum import Solution
class TestSolution(TestCase):
    def test_sliding_window_maximum_1(self):
        solution = Solution()
        nums = [1,3,-1,-3,5,3,6,7]
        expected_result = [3,3,5,5,6,7]
        k = 3
        actual_result = solution.sliding_window_maximum(nums,k)
        self.assertEqual(expected_result,actual_result)

    def test_sliding_window_maximum_2(self):
        solution = Solution()
        nums = [1]
        expected_result = [1]
        k = 1
        actual_result = solution.sliding_window_maximum(nums, k)
        self.assertEqual(expected_result,actual_result) 