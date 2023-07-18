"""
"""
from typing import List
class Solution:
    def trapping_rain_water(self, height:List[int])-> int:

        if not height: return 0

        left, right = 0, len(height) - 1
        leftmax, rightmax = height[left], height[right]
        result = 0

        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax,height[left])
                result += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                result += rightmax - height[right]
        return result