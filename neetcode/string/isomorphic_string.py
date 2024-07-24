class Solution:
    def isomorphic_string(self, s:str, t:str)->bool:
        if len(s)!= len(t):
            return False

        lookup1 = {}
        lookup2 = {}
        for i in range(len(s)):
            if s[i] in lookup1 and lookup1[s[i]]!= t[i]:
                return False
            elif t[i] in lookup2 and lookup2[t[i]] != s[i]:
                return False
            
            lookup1[s[i]] = t[i]
            lookup2[t[i]] = s[i]
        return True

def main():
    solution = Solution()
    s = "egg"
    t = "add"
    result = solution.isomorphic_string(s,t)
    print(result)

    s = "foo"
    t = "bar"
    result = solution.isomorphic_string(s,t)
    print(result)

if __name__ == "__main__":
    main()


