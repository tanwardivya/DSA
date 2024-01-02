"""
The algorithm works as follows:
- Intialize a output array same size as input array
- Update Oth index of output array with 0
- In first iteration, create a left product array i.e. output array which has product of all numbers before it ith index.
- In second iteration, fill the output array from right to left 
"""

from typing import List
class Solution:
    def product_array_except_itself(self, nums:List[int])->List[int]:
        output =[0] * len(nums)
        output[0] = 1
        for index in range(1,len(nums)):
            output[index] = nums[index -1] * output[index -1]
        right = 1
        for index in range(len(nums)-1,-1,-1):
            output[index] = output[index] * right
            right = right * nums[index]
        return output

if __name__ == '__main__':
    nums1 = [1,2,3,4]
    solution = Solution()
    result = solution.product_array_except_itself(nums = nums1)
    print(f'Product of array except itself:{result}')

    nums2 = [-1,1,0,-3,3]
    solution = Solution()
    result = solution.product_array_except_itself(nums = nums2)
    print(f'Product of array except itself:{result}')

    