from typing import List
class Solution:
    def missing_number(self, nums:List[int])->int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])

        return res

def main():
    solution = Solution()
    # nums = [3,0,1]
    nums = [1,2,3]
    result = solution.missing_number(nums)
    print(result)

if __name__ == "__main__":
    main()        