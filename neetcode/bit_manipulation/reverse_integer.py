import math


class Solution:
    def reverse_integer(self, x:int)->int:
        Min = -2147483648
        Max = 2147483647

        res = 0
        while x:
            digit = int(math.fmod(x,10)) #python dumb => -1 %10 = 9
            x = int(x//10)               #python dumb => -1 // 10 = -1
            
            if(res > Max // 10 or
               (res == Max//10 and digit >= Max % 10)):
                return 0
            if(res < Min // 10 or
               (res== Min//10 and digit <= Min % 10)):
                return 0
            res = (res * 10) + digit

        return res
    
def main():
    solution = Solution()
    x = 1234
    result = solution.reverse_integer(x)
    print(result)

if __name__ == "__main__":
    main()


