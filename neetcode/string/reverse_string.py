from typing import List
class Solution:
    def reverse_string(self,s:List[str])-> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] =s[right],s[left]
            left, right = left + 1, right - 1

def main():
    solution = Solution()
    s = ["h","e","l","l","o"]
    ans = solution.reverse_string(s)
    print(ans)
    print(s)

if __name__ =="__main__":
    main()