from typing import List
class Solution:
    def find_disappeared_numbers(self, nums:List[int])->List[int]:
       
        unique_set = set()
        for i in range(1, len(nums)+1):# +1 due to last element is not included
            unique_set.add(i)
        for num in nums:
            if num in unique_set:
                unique_set.remove(num)
        
        return list(unique_set) # convert set to list

def main():
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    result = solution.find_disappeared_numbers(nums)
    print(result)

if __name__ == "__main__":
    main()








        
