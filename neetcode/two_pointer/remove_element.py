from typing import List
class Solution:
    def remove_element(self, nums:List[int], val:int)-> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
    
def main():
    solution = Solution()
    # nums = [0,1,2,2,3,0,4,2]
    # val = 2
    nums = [1,1,2,3,4]
    val = 1
    result = solution.remove_element(nums, val)
    print("Length of array after removing element:", result)
    print("Array after removing element:", nums[:result])

if __name__ == "__main__":
    main()
