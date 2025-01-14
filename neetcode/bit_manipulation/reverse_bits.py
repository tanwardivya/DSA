class Solution:
    def reverse_bits(self, n:int)->int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31-i))

        return res
    
def main():
    solution = Solution()
    n = 0b00000000000000000000000000010101
    result = solution.reverse_bits(n)
    print(result)

if __name__ == "__main__":
    main()
    

