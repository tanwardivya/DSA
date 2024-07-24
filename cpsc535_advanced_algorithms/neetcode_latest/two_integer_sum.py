# Two Integer Sum
# Solved 
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        number_dictionary = {} #creating a dictionary/hashmap to store numbers and their corresponding indices as we iterate through nums.and mapping values with its index

#enumerate(nums) allows us to iterate through nums and simultaneously get the index (i) and the number (num)
        for i, num in enumerate(nums):# i= index, num = number
            difference = target-num
            if difference in number_dictionary:
                #If it does, return [number_dictionary[difference], i], where number_dictionary[difference] gives the index of the difference number found previously, and i is the current index.
                return [number_dictionary[difference], i]
            number_dictionary[num] = i # Store each number num in number_dictionary with its index i.
        return []

#time complexity:O(n) because iterarte through the array once and adding aeach value to our 
#hashmap which is a constant time operation and we are checking if a value exists in our 
#hashmap which is also a constant time operation
#space complexity: O(n) becuse we are potentially add every value in the hashmap               