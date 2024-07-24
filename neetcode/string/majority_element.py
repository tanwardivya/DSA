# tc = O(n), sc = O(n)
from typing import List
class Solution:
    def majority_element(self, nums:List[int])-> int:
        count = {}
        result, max_count = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            print(count[n])
            result = n if count[n]> max_count else result
            max_count = max(count[n], max_count)
            print(max_count)
        return result
        print(result)

def main():
    solution = Solution()
    nums = [3,2,3]
    final_result = solution.majority_element(nums)
    print(final_result)

if __name__ == "__main__":
    main()


    # tc = O(n), sc = O(1) from Boyer's moore ALGORITHM
    
