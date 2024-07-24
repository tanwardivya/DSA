class Solution:
    def maximum_number_of_vowels_in_substring_of_given_length(self, s:str, k:int)-> int:
        vowel_set = {'a','e','i','o','u'}
        left_ptr, count, res = 0,0,0

        for right_ptr in range(len(s)):
            count += 1 if s[right_ptr] in vowel_set else 0
            if right_ptr - left_ptr + 1 > k:
                count -= 1 if s[left_ptr] in vowel_set else 0
                left_ptr += 1
            res = max(res,count)
        return res

def main():
    solution = Solution()
    s = "abciiidef"
    k = 3
    answer = solution.maximum_number_of_vowels_in_substring_of_given_length(s,k)
    print(answer)

if __name__ == "__main__":
    main()