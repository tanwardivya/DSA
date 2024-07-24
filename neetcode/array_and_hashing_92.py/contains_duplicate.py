from typing import List
class Solution:
    def contains_duplicate(self, nums:List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False

def main():
    solution = Solution()
    nums = [1, 2, 3, 4]
    ans = solution.contains_duplicate(nums)
    print(ans)

if __name__ == "__main__":
    main()
