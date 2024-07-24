
# tc: O(2n) becasuse we are going through the sring two times
# sc : O(n)
from typing import List
class Solution:
    def concatenation_one_string_repeated_two_times(self, nums:List[int])-> List[int]:
        result = []
        # 2 is the number of time the string is repeated
        for i in range(2):
            for n in nums:
                result.append(n)
        return result
    
def main():
    solution = Solution()
    nums = [1,2,1]
    ans = solution.concatenation_one_string_repeated_two_times(nums)
    print(ans)

if __name__ == "__main__":
    main()

