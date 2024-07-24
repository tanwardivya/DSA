class Solution:
    def length_of_last_word(self, s:str)->int:
        i, length_of_word = len(s) -1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length_of_word += 1
            i -= 1
        return length_of_word

def main():
    solution = Solution()
    s = "   fly me   to   the moon  "
    ans = solution.length_of_last_word(s)
    print(ans)

if __name__ == "__main__":
    main()


   #Space Complexity O(1)
   #Memory Complexity O(N)