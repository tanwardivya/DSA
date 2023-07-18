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
