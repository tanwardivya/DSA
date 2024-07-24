from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        number_dictionary = {} #creating a dictionary to store numbers and their corresponding indices as we iterate through nums.

#enumerate(nums) allows us to iterate through nums and simultaneously get the index (i) and the number (num)
        for i, num in enumerate(nums):# i= index, num = number
            difference = target-num
            if difference in number_dictionary:
                #If it does, return [number_dictionary[difference], i], where number_dictionary[difference] gives the index of the difference number found previously, and i is the current index.
                return [number_dictionary[difference], i]
            number_dictionary[num] = i # Store each number num in number_dictionary with its index i.
        return []


def main():
    solution = Solution()
    nums = [3,4,5,6]
    target = 7
    answer = solution.twoSum(nums,target)
    print(answer)

if __name__ == "__main__":
    main()