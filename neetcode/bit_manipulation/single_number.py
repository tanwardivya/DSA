from typing import List
class Solution:
    def single_number(self, nums:List[int])-> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res

def main():
    solution = Solution()
    nums = [4,1,2,1,2]
    result = solution.single_number(nums)
    print(result)

if __name__ == "__main__":
    main()
