class Solution:
    def merge_strings_alternatively(self, word1: str, word2:str)-> str:
        i, j = 0, 0
        result = []
        while i<len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)

def main():
    solution = Solution()
    word1 = "abc"
    word2 = "pqr"
    ans = solution.merge_strings_alternatively(word1, word2)
    print(ans)

if __name__ == "__main__":
    main()