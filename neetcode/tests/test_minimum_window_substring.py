from unittest import TestCase
from sliding_window.minimum_window_substring import Solution
class TestSolution(TestCase):
    def test_minimum_window_substring_1(self):
        solution = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        expected_result = "BANC"
        actual_result = solution.minimum_window_substring(s,t)
        self.assertEqual(expected_result,actual_result)

    def test_minimum_window_substring_2(self):
        solution = Solution()
        s = "a"
        t = "a"
        expected_result = "a"
        actual_result = solution.minimum_window_substring(s,t)
        self.assertEqual(expected_result,actual_result)