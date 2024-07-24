class Solution:

    def check_kth_bit(self, n: int, k: int) -> bool:
        # Use != 0 to explicitly return True if the result is non-zero (bit is set), otherwise False
        return (n & (1 << k)) != 0 # doing the bitwise and(&) between the number and the leftshifting the number according to k 
# The expression n & (1 << k) evaluates to a number, which will be 0 if the k-th bit is not set, and a non-zero value if the k-th bit is set.
def main():
    solution = Solution()
    n = 4  # Binary representation: 100
    k = 0
    result = solution.check_kth_bit(n, k)
    print(result)  # Expected to print False, because the 0th bit (from the right) is not set in 4 (100 in binary)

if __name__ == "__main__":
    main()
