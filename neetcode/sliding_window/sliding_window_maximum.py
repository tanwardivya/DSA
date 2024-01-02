from collections import deque
from typing import List

class Solution:
    def sliding_window_maximum(self, nums:list[int], k:int) -> List[int]:
        output = []
        queue = deque() # index
        left = right = 0
        #O(n) O(n)
        while right < len(nums):
            #pop smaller values from q
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right) #index
            # remove left val from window
            if left > queue[0]:
                queue.popleft()

            if (right+1) >= k:
                output.append(nums[queue[0]])
                left += 1
            right += 1

        return output





