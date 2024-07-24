class Solution:
    def count_set_bits(self, n:int)->int:
        count  = 0
        while n > 0:
        #     if (n&1)!= 0: 
        #         count +=1
        #     n= n >> 1
        # return count
            n = n & (n-1)
        return count

def main():
    solution = Solution()
    n = 6
    result = solution.count_set_bits(n)
    print(result)

if __name__ == "__main__":
    main()