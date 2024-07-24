from typing import List
class Solution:
    def product_except_itself(self, nums: List[int])-> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

def main():
    solution = Solution()
    nums = [1,2,3,4]
    result = solution.product_except_itself(nums)
    print(result)

if __name__ == "__main__":
    main()