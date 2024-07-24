from typing import List
class Solution:
    def binary_search(self,nums:List[int],target:int)->int:
        left_ptr, right_ptr = 0, len(nums) - 1

        while left_ptr <= right_ptr:
            mid = left_ptr + ((right_ptr - left_ptr) // 2)
            if nums[mid] > target:
                right_ptr = mid - 1
            if nums[mid] < target:
                left_ptr = mid + 1

            else:
                return mid
        return -1

def main():
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    result = solution.binary_search(nums,target)
    print(result)

if __name__ == "__main__":
    main()