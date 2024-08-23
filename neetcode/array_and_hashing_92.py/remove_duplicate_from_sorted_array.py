from typing import List
class Solution:
    def remove_duplicate_from_sorted_array(self, nums:List[int])->int:
        left = 1 # start from the second element as the first element is already unique because it is already given non-decresing order in question
        for right in range(1, len(nums)): #looping from the second element, start from same position with the left & right ptr
            #check if the current element at right ptr is not equal to the previous element
            if nums[right]!= nums[right-1]: 
                # if it is not equal, replace the current element at left ptr with the current element at right ptr
                nums[left] = nums[right]
                left += 1 # for right increment for loop itself handle that case
        return left # it will also handle the case for an empty array

def main():
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = solution.remove_duplicate_from_sorted_array(nums)
    print(f"Length of the array after removing duplicates:", result)
    print("Array after removing duplicates:", nums[:result])

if __name__ == "__main__":
    main()