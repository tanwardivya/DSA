"""The provided code defines a class Solution that contains a method longest_repeating_character_replacement. This method calculates the length of the longest substring that can be formed by replacing at most k characters in the input string s with any other character.

Here's a breakdown of how the code works:
1)It initializes an empty dictionary count to keep track of the count of characters encountered so far in the sliding window.
2)It initializes a variable result to store the length of the longest valid substring found.
3)It initializes two pointers, left_window_index and right_window_index, which represent the left and right boundaries of the current sliding window, respectively.
4)It initializes a variable maxfrequency to keep track of the maximum frequency of any character encountered within the current window.
5)The code enters a loop that iterates through each character of the input string s using the right_window_index.
6)Inside the loop, it updates the count of the character at the right_window_index in the count dictionary. The get method is used to retrieve the current count and increments it by 1. This keeps track of the frequency of each character within the current window.
7)It updates maxfrequency by taking the maximum between the current maxfrequency and the count of the character at the right_window_index. This ensures that maxfrequency always stores the maximum frequency found so far within the window.
8)After updating the frequency count, it checks if the condition (right_window_index - left_window_index + 1) - maxfrequency < k is true. This condition checks if the difference between the size of the current window and the maximum frequency within the window is less than k.
9)If the condition is true, it means the current window contains more characters of the same type than allowed (k). In this case, we need to shrink the window from the left side (left_window_index) to make it valid again.
10)It decrements the count of the character at the left_window_index in the count dictionary, as we are moving the window from the left side.
11)It increments left_window_index by 1 to move the left boundary of the window one step forward.
12)The loop continues until the condition in step 8 is false, meaning the current window becomes valid again (i.e., contains at most k repeating characters).
13)After the while loop finishes, it calculates the length of the current valid substring by subtracting the left_window_index from the right_window_index and adds 1 to account for the inclusive boundaries. It updates result with the maximum between the current result and the calculated length using the max() function.
14)The loop continues, moving the right_window_index to the next character of the input string.
15)The process continues until the right_window_index reaches the end of the input string.
16)Finally, the method returns the final result, which represents the length of the longest substring that can be formed by replacing at most k characters in the input string s.
"""

class Solution:
    def longest_repeating_character_replacement(self, s:str, k:int)-> int:
        count = {}
        result = 0

        left_window_index = 0
        maxfrequency = 0

        for right_window_index in range (len(s)):
            count[s[right_window_index]] = 1 + count.get(s[right_window_index], 0)
            maxfrequency = max(maxfrequency, count[s[right_window_index]])

            while (right_window_index - left_window_index + 1) - maxfrequency > k:
                count[s[left_window_index]] -= 1
                left_window_index += 1
            result = max(result, right_window_index - left_window_index+1)

        return result



def main():
    solution = Solution()
    s = "XYYX"
    k = 2
    answer = solution.longest_repeating_character_replacement(s, k)
    print(answer)

if __name__ == "__main__":
    main()