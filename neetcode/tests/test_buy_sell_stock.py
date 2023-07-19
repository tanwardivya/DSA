from unittest import TestCase
from sliding_window.buy_sell_stock import Solution
class TestSolution(TestCase):
    def test_buy_sell_stock_1(self):
        solution = Solution()
        prices = [7,1,5,3,6,4]
        expected_result = 5
        actual_result = solution.buy_sell_stock(prices)
        self.assertEqual(expected_result,actual_result)

    def test_buy_sell_stock_2(self):
        solution = Solution()
        prices = [7,6,4,3,1]
        expected_result = 0
        actual_result = solution.buy_sell_stock(prices)
        self.assertEqual(expected_result,actual_result)
       