class Solution:

    def valid_anagram(self,s : str, t : str) -> bool:
        frequency_map = {}
        s1 = len(s)
        t1 = len(t)
        if s1 != t1:
            return False
        for character in s:
            if character in frequency_map:
                frequency_map[character] += 1
            else:
                frequency_map[character] = 1
        for character in t:
            if character in frequency_map:
                frequency_map[character] -=1
        for key, val in frequency_map.items():
            if val != 0:
                return False
        return True


if __name__ == '__main__':
    input1 = "anagram"
    input2 = "nagaram"
    solution = Solution()
    result = solution.valid_anagram(s = input1, t = input2)
    print(f"Is valid anagram: {result}")


    input1 = "cat"
    input2 = "rat"
    solution = Solution()
    result = solution.valid_anagram(s = input1, t = input2)
    print(f"Is valid anagram: {result}")

        