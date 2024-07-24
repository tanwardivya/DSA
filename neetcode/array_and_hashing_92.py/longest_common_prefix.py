from typing import List
class Solution():
    def longest_common_prefix(self, strs: list[str])->str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res

def main():
    solution = Solution()
    strs = ["flower","flow","flight"]
    ans = solution.longest_common_prefix(strs)
    print(ans)

if __name__ == "__main__":
    main()

        