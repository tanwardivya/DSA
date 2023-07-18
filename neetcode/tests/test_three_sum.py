from unittest import TestCase
from two_pointer.three_sum import Solution
class TestSolution(TestCase):
    def test_three_sum_1(self):
        solution = Solution()
        nums = [-1,0,1,2,-1,-4]
        expected_result = [[-1,-1,2],[-1,0,1]]
        actual_result = solution.three_sum(nums)
        self.assertCountEqual(actual_result, expected_result)

    def test_three_sum_2(self):
        solution = Solution()
        nums = [0,1,1]
        expected_result = []
        actual_result = solution.three_sum(nums)
        self.assertCountEqual(actual_result,expected_result)