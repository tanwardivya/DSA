class Solution:
    def hasAllCodes(self, s:str, k:int)-> bool:
        code_set = set()

        for i in range(len(s) - k + 1):
            code_set.add(s[i:i+k])
        
        return len(code_set) == 2 ** k

def main():
    solution = Solution()
    s = "00110110"
    k = 2
    answer = solution.hasAllCodes(s,k)
    print(answer)

if __name__ == "__main__":
    main()






    

