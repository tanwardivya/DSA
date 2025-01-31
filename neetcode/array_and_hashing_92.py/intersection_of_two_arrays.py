from typing import List


class Solution:
    def intersection_of_two_arrays(self, nums1:List[int],nums2:List[int])->List[int]:
        seen = set(nums2)
        res = []

        for num in nums1:
            if num in seen:
                res.append(num)
                seen.remove(num)

        return res
    
def main():
    solution = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    result = solution.intersection_of_two_arrays(nums1,nums2)
    print(result)

if __name__ == "__main__":
    main()
