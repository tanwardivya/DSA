class Solution:
    def no_of_one_bits_optimal(self, n:int)->int:
        res = 0
        while n:
            n &= n-1
            res += 1

        return res
    
def main():
    solution = Solution()
    n =0b10000001
    result = solution.no_of_one_bits_optimal(n)
    print(result)

if __name__ == "__main__":
    main()
