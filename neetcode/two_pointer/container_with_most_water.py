""" 1)This code defines a class Solution that contains a method container_with_most_water. The purpose of this method is to find the container with the most water in a given list of heights.

Here's a breakdown of how the code works:
2)The code starts with a commented-out brute force approach that has a time complexity of O(n^2). This approach involves nested loops to check all possible pairs of lines and calculate the area of water between them. However, this approach is not used in the code.
3)The code then introduces a linear time solution with a time complexity of O(n) to find the maximum area. It initializes the result variable to 0, which will store the maximum area found.
4)It initializes two pointers, left and right, to point to the start and end of the height list, respectively.
5)The code enters a while loop that continues as long as the left pointer is less than the right pointer. This loop iterates inward from both ends of the height list.
6)Inside the loop, it calculates the area of water between the lines at the current left and right indices using the formula (right - left) * min(height[left], height[right]).
7)It updates the result variable by taking the maximum between the current result and the calculated area using the max() function. This ensures that result always stores the maximum area found so far.
8)Next, it compares the heights at the left and right indices. If the height at the left index is less than the height at the right index, it means the current left line is shorter. In this case, it increments the left pointer by 1 to consider the next line with potentially greater height.
9)If the height at the left index is greater than or equal to the height at the right index, it means the current right line is shorter or equal. In this case, it decrements the right pointer by 1 to consider the next line with potentially greater height.
10)The loop continues until the left and right pointers meet or cross each other. This means all possible pairs of lines have been considered, and the maximum area has been calculated.
11)Finally, the method returns the final result, which represents the maximum area of water that can be contained between any pair of lines in the height list.
12)Overall, this code uses a two-pointer approach to efficiently find the maximum area of water. By iteratively considering the shorter line and adjusting the pointers, it narrows down the search space and finds the optimal solution in linear time.
"""

from typing import List
from unittest import result
class Solution:
    def container_with_most_water(self,height:List[int]) -> int:
        # # brute force approach ->O(n^2)
        # result = 0

        # for left in range(len(height)):
        #     for right in range(left+1, len(height)):
        #         area = (right - left) * min(height[left], height[right])
        #         result = max(result,area)

        # return result

    # Linear time solution O(n)
        result = 0
        left, right  = 0, len(height)-1

        while left < right:
            area = (right - left)* min(height[left], height[right])
            result = max(result,area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
