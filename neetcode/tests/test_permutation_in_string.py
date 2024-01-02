from unittest import TestCase
from sliding_window.permutation_in_string import Solution
class TestSolution(TestCase):
    def test_permutation_in_string_1(self):
        solution = Solution()
        s1 = "ab" 
        s2 = "eidbaooo"
        expected_result = True
        actual_result = solution.permutation_in_string(s1,s2)
        self.assertEqual(expected_result,actual_result)

    def test_permutation_in_string_2(self):
        solution= Solution()
        s1 = "ab"
        s2 = "eidboaoo"
        expected_result = False
        actual_result = solution.permutation_in_string(s1,s2)
        self.assertEqual(expected_result,actual_result)

