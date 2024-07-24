class Solution:
    def remove_all_adjacent_duplicates(self, s:str, k:int)-> str:
        stack = [] # [char, count], this will create

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])

            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, count in stack:
            res += (char * count)
        return res

def main():
    solution = Solution()
    s = "deeedbbcccbdaa"
    k = 3
    result = solution.remove_all_adjacent_duplicates(s,k)
    print(result)

    s = "abcd"
    k = 2
    result = solution.remove_all_adjacent_duplicates(s,k)
    print(result)

    s = "deeedbbcccbd"
    k = 3
    result = solution.remove_all_adjacent_duplicates(s,k)
    print(result)

    s = "pbbcggttciiippooaais"
    k = 2
    result = solution.remove_all_adjacent_duplicates(s,k)
    print(result)

if __name__ == "__main__":
    main()


#description

# class Solution:: This line defines a class named Solution.

# def remove_all_adjacent_duplicates(self, s:str, k:int) -> str:: This line defines a method within the Solution class named remove_all_adjacent_duplicates. It takes two parameters: s, which is a string representing the input string, and k, which is an integer representing the number of adjacent duplicates to remove.

# stack = []: This line initializes an empty list named stack. This stack will be used to keep track of characters and their counts.

# for c in s:: This line starts a loop over each character c in the input string s.

# if stack and stack[-1][0] == c:: This line checks if the stack is not empty (stack) and if the last character in the stack (stack[-1][0]) is equal to the current character c.

# stack[-1][1] += 1: If the current character is the same as the last character in the stack, it increments the count of that character in the stack.

# else:: If the current character is different from the last character in the stack, this line executes.

# stack.append([c, 1]): This line appends a list [c, 1] to the stack, representing a new character c with a count of 1.

# if stack[-1][1] == k:: This line checks if the count of the last character in the stack is equal to k.

# stack.pop(): If the count of the last character in the stack is equal to k, this line removes that character from the stack.

# res = "": This line initializes an empty string named res. This will be used to construct the final result string.

# for char, count in stack:: This line starts a loop over each character and its count in the stack.

# res += (char * count): This line appends the character char repeated count times to the res string.

# return res: This line returns the final result string res.

# def main():: This line defines a function named main.

# solution = Solution(): This line creates an instance of the Solution class named solution.

# s = "deeedbbcccbdaa": This line defines the input string s.

# k = 3: This line defines the value of k, which represents the number of adjacent duplicates to remove.

# result = solution.remove_all_adjacent_duplicates(s, k): This line calls the remove_all_adjacent_duplicates method of the solution instance with the input string s and value of k.

# print(result): This line prints the result returned by the remove_all_adjacent_duplicates method.

# if __name__ == "__main__":: This line checks if the script is being run as the main program.

# main(): This line calls the main function if the script is being run as the main program.