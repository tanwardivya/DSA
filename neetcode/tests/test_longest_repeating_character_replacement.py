from unittest import TestCase
from sliding_window.longest_repeating_character_replacement import Solution
class TestSolution(TestCase):
    def test_longest_repeating_character_replacement(self):
        solution = Solution()
        s = "ABABBA"
        expected_result = 5
        k = 2
        actual_result = solution.longest_repeating_character_replacement(s, k)
        self.assertEqual(expected_result,actual_result)

    def test_longest_repeating_character_replacement_1(self):
        solution = Solution()
        s = "ABAB"
        k = 2
        expected_result = 4
        actual_result = solution.longest_repeating_character_replacement(s,k)
        self.assertEqual(expected_result,actual_result)

    def test_longest_repeating_character_replacement_2(self):
        solution = Solution()
        s = "AABABBA"
        k = 1
        exepected_result = 4
        actual_result = solution.longest_repeating_character_replacement(s,k)
        self.assertEqual(exepected_result,actual_result)
