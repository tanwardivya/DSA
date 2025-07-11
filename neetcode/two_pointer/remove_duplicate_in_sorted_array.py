from typing import List
class Solution:
    def remove_duplicate(self, nums: List[int])->int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right -1]:
                nums[left] = nums[right]
                left += 1

        return left
    
def main():
    solution = Solution()
    nums = [0,1,1,2,3,3,3,4,4,4,4,5]
    result = solution.remove_duplicate(nums)
    print("Length of array after removing duplicates:", result)

if __name__ == "__main__":
    main()