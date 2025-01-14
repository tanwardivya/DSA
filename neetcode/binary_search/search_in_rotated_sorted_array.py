from typing import List
class Solution:
    def search_in_rotated_sorted_array(self, nums:List[int], target:int)->int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else: 
                    right = mid - 1

            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

def main():
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = solution.search_in_rotated_sorted_array(nums,target)
    print(result)

if __name__ == "__main__":
    main()

            