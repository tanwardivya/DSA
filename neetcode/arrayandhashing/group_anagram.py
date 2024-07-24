"""
This algorithm works as follows:
1. initialize 
"""


# class Solution:
#     def group_anagram(self, strs:List[str]) -> List[List[str]]:
        # """Group into anagram from given list of words.

        # Args:
        #     strs (List[str]): List of words

        # Returns:
        #     List[List[str]]: List of anagrams grouped into a list.
        # """
        # # Look up dictionary to store word as a key and anagrams as a value
        # lookup_map:Dict[str, List[str]] = {}
        # for word in strs:
        #     sort_word =''.join(sorted(word)) 
        #     if sort_word in lookup_map:
        #         lookup_map[sort_word].append(word)
        #     else:
        #         lookup_map[sort_word] = [word]
        # return list(lookup_map.values())

from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            ans[tuple(count)].append(s)
        return list(ans.values())


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]  
    solution = Solution()   
    result = solution.groupAnagrams(strs) 
    print(f"Group of anagrams:{result}")         