class Solution:
    def no_of_1_bits(self, n:int)->int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1

        return res
    
def main():
    solution = Solution()
    #n = 0b10111
    n = 0b01111111111111111111111111111101 
    result = solution.no_of_1_bits(n)
    print(result)

if __name__ == "__main__":
    main()


# The input 01111111111111111111111111111101 needs to be interpreted carefully. 
# In Python, if you write it as is, it will raise a syntax error due to the leading 
# zero. If you intend to use this as a binary number, you should use the 0b prefix. 
# Let's address how to handle this input. 0b01111111111111111111111111111101 

# note
#If the number is provided as a string (e.g., "01111111111111111111111111111101"), 
# you can convert it to an integer using the int function:python
# Copy code
# binary_str = "01111111111111111111111111111101"
# n = int(binary_str, 2)
# This will correctly interpret the string as a binary number.
