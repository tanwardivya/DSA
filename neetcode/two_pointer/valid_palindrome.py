class Solution:
    def valid_palindrome(self, s:str)-> bool:
        # i=0
        # j=len(s)-1
        # s = s.lower()
        # while i <= j:
        #     if not s[i].isalnum():
        #         i += 1
        #     elif not s[j].isalnum():
        #         j -= 1
        #     else:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        # return True

        #version 2
       
  
        left, right = 0, len(s) - 1

         while left < right:
            while left < right and not self.alphaNumeric(s[left]):
                left += 1
            while right > left and not self.alphaNumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        
        return True

    def alphaNumeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
def main():
    solution = Solution()
    s = "Was it a car or a cat I saw?"
 
    answer = solution.valid_palindrome(s)
    print(answer)

if __name__ == "__main__":
    main()

