from typing import List
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        print(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
def main():
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    answer = solution.longestCommonPrefix(strs)

if __name__ == "__main__":
    main()
