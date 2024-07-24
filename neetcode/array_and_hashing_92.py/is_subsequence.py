class Solution:
    def is_subsequence(self, s:str, t:str) -> bool:
        i, j = 0, 0

        while i< len(s) and j< len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False
def main():
    solution = Solution()
    s= 'abc'
    t = 'agdbhc'
    ans = solution.is_subsequence(s,t)
    print(ans)

if __name__ == "__main__":
    main()
