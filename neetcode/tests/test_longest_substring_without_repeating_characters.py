from unittest import TestCase
from sliding_window.longest_substring_without_repeating_characters import Solution
class TestSolution(TestCase):
    def test_longest_substring_without_repeating_characters(self):
        soluton = Solution()
        s = "abcabcbb"
        expected_result = 3
        actual_result = soluton.longest_substring_without_repeating_characters(s)
        self.assertEqual(expected_result,actual_result)

    def test_longest_substring_without_repeating_characters_1(self):
        solution = Solution()
        s= "bbbbb"
        expected_result = 1
        actual_result = solution.longest_substring_without_repeating_characters(s)
        self.assertEqual(expected_result,actual_result)

    def test_longest_substring_without_repeating_characters_2(self):
        solution = Solution()
        s = "pwwkew"
        expected_result = 3
        actual_result = solution.longest_substring_without_repeating_characters(s)
        self.assertEqual(expected_result,actual_result)
