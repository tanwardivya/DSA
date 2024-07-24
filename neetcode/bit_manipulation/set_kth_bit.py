class Solution:
    def set_kth_bit(self, n:int, k:int)->int:
        return (n|(1<<k))

def main():
    solution = Solution()
    n = 10
    k = 2
    result = solution.set_kth_bit(n,k)
    print(result)

if __name__ == "__main__":
    main()


# The expression return (n | (1 << k)) is a bit different from checking if a bit is set. Instead, it's used to set the k-th bit of the number n to 1. Let's break down how it works:

# Bitwise OR (|): The bitwise OR operation takes two bit patterns of equal length and performs the logical inclusive OR operation on each pair of corresponding bits. The result in each position is 1 if the first bit is 1 or the second bit is 1 or both bits are 1; otherwise, the result is 0. For example:

# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1
# Left Shift (<<): The left shift operation 1 << k shifts the number 1 to the left by k positions. This effectively means creating a value where the k-th bit is set to 1, and all other bits are 0. For example, if k = 3, then 1 << 3 results in 1000 in binary, which is 8 in decimal.

# Combining with OR: When you perform the bitwise OR operation between n and (1 << k), you're effectively setting the k-th bit of n to 1, regardless of its previous value. This is because OR-ing any bit with 1 will always result in 1, thereby setting that bit. If the bit was already 1, it remains 1; if it was 0, it changes to 1.

# Here's an example to illustrate this:

# Let's say n = 4 (which is 100 in binary), and you want to set the 1st bit (counting from 0 from the right).
# 1 << 1 gives 10 in binary (which is 2 in decimal).
# Now, you OR this with n:
# n = 4 in binary: 100
# 1 << 1 in binary: 010
# n | (1 << 1) in binary: 110 (which is 6 in decimal).
# So, return (n | (1 << k)) doesn't check if a bit is set; instead, it returns a new number with the k-th bit set to 1.