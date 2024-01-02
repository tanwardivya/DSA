"""
"""
class Solution:
    def minimum_window_substring(self, s:str, t:str)-> str:
        if t == " ": return " " 

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if(right-left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window [s[left]] < countT[s[left]]:
                    have -=1
                
                left += 1
        
        left, right = res
        return s[left:right +1] if resLen != float("infinity") else ""
