class Solution:
    def is_anagram(self, s:str, t:str)-> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for character in countS:
            if countS[character] != countT.get(character,0):
                return False
        return True

def main():
    solution = Solution()
    s = "racecar"
    t = "carrace"
    ans = solution.is_anagram(s,t)
    print(ans)

if __name__ == "__main__":
    main()
