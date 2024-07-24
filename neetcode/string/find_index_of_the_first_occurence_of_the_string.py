class Solution:
    def strStr(self, haystack:str, needle:str)->int:
        for i in range(len(haystack)- len(needle)+1):
            window_string = haystack[i:i+len(needle)]
            if window_string == needle:
                return i
        return -1

def main():
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    result = solution.strStr(haystack,needle)
    print(result)

if __name__ == "__main__":
    main()