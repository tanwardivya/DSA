from typing import List
class Solution:
    def remove_element(self, nums:List[int], val:int)-> int:
        k = 0 #intializing the ptr
        for i in range(len(nums)): #looping through the array
            if nums[i]!= val: #if the current element is not equal to the given value
                nums[k] = nums[i] # place the current element at the kth position
                k += 1 # for right increment for loop itself handle that case

        for i in range(k, len(nums)): # for i in range(k, len(nums)):  # if k is less than the length of the array, assign 0 to the remaining elements
            nums[i] = 0  # to remove the duplicates in the list
        return k # it will return the length of the array after removing duplicates

def main():
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    result = solution.remove_element(nums, val)
    print(f"Length of the array after removing {val}:", result)
    print("Array after removing duplicates:", nums[:result])
    print("Array after removing duplicates:", nums)


if __name__ == "__main__":
    main()
        
