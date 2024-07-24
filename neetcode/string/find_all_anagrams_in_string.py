from typing import List
class Solution:
    def find_all_anagrams(self, s:str, p:str) -> List[int]:
        if len(p) > len(s): return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if pCount == sCount else []
        left = 0
        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1     

            if sCount[s[left]] == 0:
                sCount.pop(s[left])

            left += 1
            if sCount == pCount:
                res.append(left)

        return res

def main():
    solution = Solution()
    s = "cbaebabacd"
    p = "abc"

    answer = solution.find_all_anagrams(s,p)
    print(answer)

if __name__ == "__main__":
    main()

