from typing import List
class Solution:
    def monotonic_array(Self,nums:List[int])->List[int]:
        n = len(nums)
        increase = True
        for i in range(1,n):
            if nums[i] < nums[i - 1]:
                increase = False
                break

        if increase:
            return True
        
        for i in range(1,n):
            if nums[i] > nums[i - 1]:
                decrease = False
                break
        return decrease

def main():
    solution = Solution()
    nums = [1,2,2,3]
    result = solution.monotonic_array(nums)
    print(result)

if __name__ == "__main__":
    main()