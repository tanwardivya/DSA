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
    # strs = ["eat","tea","tan","ate","nat","bat"]  
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    solution = Solution()   
    result = solution.groupAnagrams(strs) 
    print(f"Group of anagrams:{result}")