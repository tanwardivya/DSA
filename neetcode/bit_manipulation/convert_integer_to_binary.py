class Solution:
    def integer_to_binary(self, n:int)->str:
    
        ans = ""
        while n>0:
           remainder = n % 2
           ans = str(remainder) + ans
           n = n // 2
        return "".join(ans)

def main():
    solution = Solution()
    n = 23
    result = solution.integer_to_binary(n)
    print(result)

if __name__ == "__main__":
    main()

        