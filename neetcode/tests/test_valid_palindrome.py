from unittest import TestCase
from two_pointer.valid_palindrome import Solution
class TestSolution(TestCase):

    def test_valid_palindrome_1(self):
        solution = Solution()
        expected_result = True
        s1 = "A man, a plan, a canal: Panama"
        actual_result = solution.valid_palindrom(s1)
        self.assertEqual(actual_result,expected_result)

    def test_valid_palindrome_2(self):
        solution = Solution()
        expected_result = False
        s2 = "race a car"
        actual_result = solution.valid_palindrom(s2)
        self.assertEqual(actual_result,expected_result) 

    def test_valid_palindrome_3(self):
        solution = Solution()
        expected_result = True
        s = ".,"
        actual_result = solution.valid_palindrom(s)
        self.assertEqual(actual_result,expected_result) 
        