"""1)Initially defines a class Solution that contains a method three_sum. The purpose of this method is to find all unique triplets in the nums list that sum up to zero.

Here's a breakdown of how the code works:
2)It initializes an empty list called result that will store the resulting triplets.
3)The code sorts the nums list in ascending order. Sorting the list helps in avoiding duplicates and simplifies the process of finding triplets with a specific sum.
4)It iterates over the elements of the nums list using the enumerate function, which provides both the index i and the value a of each element.
5)Inside the loop, it checks if the current element a is the same as the previous element nums[i-1] (to avoid duplicates). If it is, the loop skips to the next iteration using the continue statement.
6)If the current element is not a duplicate, it initializes two pointers, left and right, to search for pairs that sum up to the negation of the current element (-a).
7)It enters a while loop that continues as long as the left pointer is less than the right pointer.
8)Inside the loop, it calculates the sum of the three elements: a, nums[left], and nums[right].
9)If the sum is greater than zero, it means the right element is too large, so it decrements the right pointer to consider a smaller element in the next iteration.
10)If the sum is less than zero, it means the left element is too small, so it increments the left pointer to consider a larger element in the next iteration.
11)If the sum is equal to zero, it means we have found a triplet that sums up to zero. It appends the triplet [a, nums[left], nums[right]] to the result list.
12)After appending the triplet, it increments the left pointer to consider the next different element (skipping duplicates). This is done using a nested while loop that continues as long as the current left element is the same as the previous one nums[left - 1].
13)Finally, after the while loop finishes, it returns the result list containing all the unique triplets that sum up to zero.
"""

from typing import List
class Solution:
    def three_sum(self, nums:List[int])-> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            left,right = i+1, len(nums) -1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return result                 