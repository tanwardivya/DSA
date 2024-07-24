# using memory complexity O(1)
from typing import List
class Solution:
    def finding_disappeared_numbers(self,nums:List[int])-> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):# enumerate helps us go through the index and value simultaneosly
            if n > 0:
                res.append(i + 1)
        return res

def main():
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    result = solution.finding_disappeared_numbers(nums)
    print(result)

if __name__ == "__main__":
    main()


