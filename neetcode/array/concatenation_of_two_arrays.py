from typing import List
class Solution:
    def concatenation_of_two_arrays(self, nums:List[int])->List[int]:
        result = []
        for i in range(2):
            for n in nums:
                result.append(n)
        return result

def main():
    solution = Solution()
    nums = [1,2,1]
    answer = solution.concatenation_of_two_arrays(nums)
    print(answer)

if __name__ == "__main__":
    main()
            