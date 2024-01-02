from typing import List


class Solution:

    def two_sum(self, nums : List[int] , target : int)-> List[int]:
        """Sum of two numbers.

        Args:
            num (int): List of integers
            target (int): Target value

        Returns:
            int: return the indices of the two numbers that added upto the target value.
        """
        index_map = {}
        for index in range(0, len(nums)):
            number_to_be_searched = target - nums[index]
            if number_to_be_searched in index_map:
                return [index_map[number_to_be_searched] , index]
            index_map[nums[index]]  = index  
        return [-1]

if __name__ == '__main__':
    list1 = [2,7,11,15]
    target = 9
    solution = Solution()  
    result = solution.two_sum(nums = list1, target  = target)
    print(f"Return indices of two numbers that added up to target: {result} ")      

    list2 = [3, 2, 4]
    target = 6
    solution = Solution()  
    result = solution.two_sum(nums = list2, target  = target)
    print(f"Return indices of two numbers that added up to target: {result} ")  

    list3 = [3,1,2,1]
    target = 6
    solution = Solution()  
    result = solution.two_sum(nums = list3, target  = target)
    print(f"Return indices of two numbers that added up to target: {result} ")        