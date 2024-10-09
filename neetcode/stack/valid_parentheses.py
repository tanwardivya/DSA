class Solution:
    def valid_parentheses(self, s:str) -> bool:
        stack = []
        close_to_open = {")":"(", "}":"{", "]":"["}

        for character in s:
            if  character in close_to_open:
                if stack and stack[-1] == close_to_open[character]:
                    stack.pop()

                else:
                    return False
            
            else: 
                stack.append(character)
        
        return True if not stack else False

def main():
    solution = Solution()
    s = "([{}])"
    ans = solution.valid_parentheses(s)
    print(ans)

if __name__ == "__main__":
    main()


