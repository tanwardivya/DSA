from typing import List
class Solution:
    def sort_colors(self, nums:List[int])->List[int]:
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

def main():
    # nums = [2, 0, 2, 1, 1, 0]
    nums = [1, 0, 1, 2]
    solution = Solution()
    res = solution.sort_colors(nums)
    print(res)

if __name__ == "__main__":
    main()

# #Time Complexity (TC)
# The while mid <= high: loop scans each element at most once (since mid is always moving forward except when you swap with high for a 2, but even then, each index is visited at most once as either mid or high).

# Every operation inside the loop is O(1).

# So, the entire array of length n is traversed at most once.

# TC:O(n)
# Space Complexity (SC)
# All operations are done in-place (no extra data structures).

# Only a constant number of variables (low, mid, high) are used.

# SC:O(1)

#Tc: O(n)#Sc: O(1)



