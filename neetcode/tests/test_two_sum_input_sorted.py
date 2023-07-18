from unittest import TestCase
from two_pointer.two_sum_input_sorted import Solution
class TestSolution(TestCase):
    def test_two_sum_input_sorted_1(self):
        solution = Solution()
        expected_result = [1,2]
        numbers = [2,7,11,15]
        target = 9
        actual_result = solution.two_sum_input_sorted(numbers, target)
        self.assertCountEqual(actual_result,expected_result)

    def test_two_sum_input_sorted_2(self):
        solution = Solution()
        expected_result = [1,3]
        numbers = [2,3,4]
        target = 6
        actual_result = solution.two_sum_input_sorted(numbers, target)
        self.assertCountEqual(actual_result,expected_result)

    def test_two_sum_input_sorted_3(self):
        solution = Solution()
        expected_result = [1,2]
        numbers = [-1,0]
        target = -1
        actual_result = solution.two_sum_input_sorted(numbers,target)
        self.assertCountEqual(actual_result, expected_result)



        
