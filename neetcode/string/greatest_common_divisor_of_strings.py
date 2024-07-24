class Solution:
    def gcd_of_strings(self, str1: str, str2: str)-> str:
        len1, len2 = len(str1), len(str2)

        def is_divisor(l):
            if len1 % l or len2 % l:
                return False

            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if is_divisor(l):
                return str1[:l]
        return ""

def main():
    solution = Solution()
    str1 = "LEET"
    str2 = "CODE"
    answer = solution.gcd_of_strings(str1,str2)
    print(answer)

if __name__ == "__main__":
    main()




#dry run
# Step 1: Initialization
# str1 = "ABCABC"
# str2 = "ABC"
# The Solution class is instantiated, and its method gcd_of_strings is called with str1 and str2.
# Step 2: Calculate Lengths
# len1 = len(str1) = 6
# len2 = len(str2) = 3
# Step 3: Define is_divisor Function
# This function checks if a given length l can be a divisor of both strings in the sense that both strings can be constructed by repeating a substring of length l.

# Step 4: Loop Through Possible Divisors
# The loop starts with l = min(len1, len2) = 3 and decrements l until it reaches 1. For each l, it checks if l is a divisor of both string lengths and if the strings can be constructed by repeating a substring of length l.

# First Iteration (l = 3)
# Check if len1 % l == 0 and len2 % l == 0:
# 6 % 3 == 0 and 3 % 3 == 0 (True for both)
# Calculate f1 = len1 // l = 6 // 3 = 2
# Calculate f2 = len2 // l = 3 // 3 = 1
# Check if str1[:l] * f1 == str1 and str1[:l] * f2 == str2:
# str1[:3] * 2 = "ABC" * 2 = "ABCABC" which equals str1
# str1[:3] * 1 = "ABC" * 1 = "ABC" which equals str2
# Since both conditions are met, is_divisor(l) returns True.
# Since is_divisor(l) returned True for l = 3, the loop ends, and str1[:l] = "ABC" is returned as the greatest common divisor (GCD) of the strings.

# Step 5: Return Value
# The method gcd_of_strings returns "ABC" as the GCD of the strings str1 and str2.

# Step 6: Print the Answer
# The main function prints the answer, which is "ABC".

# Conclusion
# The dry run of the program with the inputs str1 = "ABCABC" and str2 = "ABC" correctly finds that the greatest common divisor of the strings in terms of repeated substrings is "ABC", and this is printed as the output.
