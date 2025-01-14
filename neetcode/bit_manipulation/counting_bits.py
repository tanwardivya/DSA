from typing import List 
class Solution:
    def counting_bits(self, n:int)->List[int]:
        dp = [0] *(n+1)
        offset = 1# highest power of 2

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1+ dp[i-offset]

        return dp
    
def main():
    solution = Solution()
    n = 4
    result = solution.counting_bits(n)
    print(result)

if __name__ == "__main__":
    main()
