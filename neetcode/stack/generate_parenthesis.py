class GenerateParenthesis:
    def generateParenthesis(self, n:int)->list[str]:

        stack = [] #creating a stack to hold the parenthesis
#creating a result variable which will have the list of valid parenthesis
        result = []

# doing it recursively so putting a function inside another function. so if user has
# this then no need to add above two variables into the function because this is 
# nested inside here. and there is no need to pass 'n' either, but there is need to
# pass the openN and closedN count to call openN and closedN because it is the base
# case.
        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

# if i want to add a open parenthesis we have tofirst check that our open 
# parenthesis count is less than 'n' if that's true, we can append open parenthesis
# to the stack, then we can recusively backtrack and but if we do that we have to 
# increment our open count by 1 and closedremains the same. after that backtracking
# returns though we do have to update our stack becoz we only have a single single 
# stack variable. remember we're not passing this stack into every single call, this
#stack is basically a global variable  so every time we're done with the with 
# backtracking. we have to pop the character that we just added to the stack.

            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
#if i want to add a closing parenthesis we have to first check that our closed count 
# parenthesis count is less than open parenthesis count if that's true, we can 
# append closed parenthesis to the stack, and then we can cal our backtracking fxn 
# and leave the open count same this time and increment the closed count by 1 as
# before. there is also a need to cleanup so by updating the stack by poping the 
# character that is recently added  
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return result

def main():
    gp = GenerateParenthesis()
    result = gp.generateParenthesis(3)
    
    print(result)

if __name__ == "__main__":
    main()