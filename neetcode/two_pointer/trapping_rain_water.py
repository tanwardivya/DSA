""" this algorithm works as follows:
1) Initially check that if the given list of heights is empty return zero this is  aspecial case.
2) Initialise two pointers left  and right to zero and the end of the indices of list height
3)and two more pointers leftmax and right max for storing the maximum heights from the left and right sides of the list
4)and result to zero and it will store the total area of the water between lines. 
5)now in a while loop, check for as long as the left is less than the right it will iterate towards the center of the list.
6) inside the while loop there is a if condition checks for the condition that left max is less than the right max indicates that the left height from left is greater than the right height in the list sofar.
7)if the condition is true left is incremented by 1 and upadtes the leftmax variable to the maximum value between the current leftmax and height at the new left index.
8)It calculates the difference between the updated leftmax and the height at the new left index and adds this difference to the result variable. This difference represents the amount of water that can be contained between the lines at the current left and left - 1 indices.
9)If the condition is false, it means the line at the right pointer is shorter or equal to the line at the left pointer. It decrements the right pointer by 1 and updates the rightmax variable to the maximum value between the current rightmax and the height at the new right index.
10)It calculates the difference between the updated rightmax and the height at the new right index and adds this difference to the result variable. This difference represents the amount of water that can be contained between the lines at the current right and right + 1 indices.
11)After the loop finishes, the method returns the final result, which represents the maximum area of water that can be contained between any pair of lines in the height list.
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