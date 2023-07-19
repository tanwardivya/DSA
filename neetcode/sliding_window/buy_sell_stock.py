"""The code defines a class Solution that contains a method buy_sell_stock. This method calculates the maximum profit that can be obtained by buying and selling a stock within the given list of prices.

Here's a breakdown of how the code works:

1)It initializes two pointers, left and right, which represent the indices for buying and selling the stock, respectively.
2)It initializes the max_profit variable to 0, which will store the maximum profit obtained.
3)The code enters a while loop that continues as long as the right pointer is within the bounds of the prices list.
4)Inside the loop, it checks if the price at the left index is less than the price at the right index. This condition ensures that there is a potential profit to be made by buying at the left index and selling at the right index.
5)If the condition is true, it calculates the profit by subtracting the price at the left index from the price at the right index (prices[right] - prices[left]).
6)It updates the max_profit variable by taking the maximum between the current max_profit and the calculated profit using the max() function. This ensures that max_profit always stores the maximum profit found so far.
7)If the condition in step 4 is false, it means the price at the left index is greater than or equal to the price at the right index. In this case, there is no potential profit, so it updates the left pointer to the right index. This means we start considering a new potential buying price.
8)It increments the right pointer by 1 to move to the next index, continuing the loop.
9)The loop continues until the right pointer reaches the end of the prices list.

Finally, the method returns the final max_profit, which represents the maximum profit that can be obtained by buying and selling the stock based on the given prices.
"""
from typing import List
class Solution:
    def buy_sell_stock(self, prices:List[int])-> int:
        # left = buy, right = sell
        left, right = 0, 1
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)
            
            else:
                left = right
            right  += 1
        return max_profit

