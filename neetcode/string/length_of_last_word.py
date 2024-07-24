class Solution:
    def length_of_last_word(self, s:str)-> int:
        i = len(s)-1 # index of last character because we are satrting from the last character
        length = 0 # length of the word
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


        # tc = O(n)
        # sc = O(1)
def main():
    solution = Solution()
    s = "   fly me   to   the moon  "
    result = solution.length_of_last_word(s)
    print(result)

if __name__ == "__main__":
    main()

    
