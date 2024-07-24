from typing import List
class Solution:
    def missing_number(self, nums: List[int])-> int:
        result = len(nums)
        for i in range(len(nums)):
            result += (i-nums[i])
            
        return result

def main():
    solution = Solution()
    nums = [3,0,4,2]
    res = solution.missing_number(nums)
    print(res)

if __name__ == "__main__":
    main()

#T.C = O(2n)
#S.C = O(1)