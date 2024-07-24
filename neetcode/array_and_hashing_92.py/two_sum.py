from typing import List
class Solution:
    def two_sum(self,nums:List[int], target:int)-> List[int]:
        number_dictionary = {}

        for i, num, in enumerate(nums):
            diff = target - num
            if diff in number_dictionary:
                return[number_dictionary[diff], i]
            number_dictionary[num] = i
        
        return []

def main():
    solution = Solution()
    nums = [3,4,5,6]
    target = 7
    ans = solution.two_sum(nums, target)
    print(ans)

if __name__ == "__main__":
    main()

#time complexity:O(n) because iterarte through the array once and adding aeach value to our 
#hashmap which is a constant time operation and we are checking if a value exists in our 
#hashmap which is also a constant time operation
#space complexity: O(n) becuse we are potentially add every value in the hashmap 