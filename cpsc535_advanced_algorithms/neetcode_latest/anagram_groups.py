# Anagram Groups
# Solved 
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 #creating a hashmap res, here we are mapping the character count of each string to list of anagrams
        res = defaultdict(list)
# going through every string that we're given in the input
        for s in strs: 
#we want to count how many of each character it has, so initially we have a array and we have o(zero) 
#in this array, we are going to have 26 zeroes one for each character from lower case a to lowercase z      
            count= [0] * 26

# now we want to go through every single character in each string and want to count how many of each 
#character map from (a to index 0) and (z to index 25). so this can be done by using the ascii 
#value of charcter minus the ascii value of lowercase "a" and increment that by 1 to count how many
#character we have:
            for character in s:
                count[ord(character) - ord("a")] += 1

#in our result for the particular count we want to append the string s, so that we get the group 
#of the anagram for this particular count together. but what if this count doesn't exist right 
#now for that we take the default value of res dictionary to a default dictionary or a default 
#hashmap where the default value is a list, and it can also handle one edge case.  
#now count is list but in python lists cannot be keys so we are changing to tuple becoz tuples 
#are non mutable.
            res[tuple(count)].append(s)
#now in our dictionary we have grouped the anagrams together so we can take the result.values,
#because we don't want the keys. so we just return the resulted values
        return res.values()

        

        