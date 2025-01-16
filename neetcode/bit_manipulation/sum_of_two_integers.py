class Solution:
    def sum_of_two_integers_without_plus_minus_sign(self, a:int, b:int)-> int:
        mask = 0xffffffff
        max_int = 0xfffffff

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) &mask
            b = carry&mask

        return a if a <= max_int else ~(a^mask)
    
    
def main():
    solution = Solution()
    a = 9
    b = 11
    result = solution.sum_of_two_integers_without_plus_minus_sign(a,b)
    print(result)

if __name__ == "__main__":
    main()
