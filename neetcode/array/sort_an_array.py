
from typing import List
class Solution:
    def sort_array(self,nums:List[int])->List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k, = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def merge_sort(arr, l, r):
            if l == r:
                return arr
            
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr

        return merge_sort(nums, 0, len(nums) - 1)

def main():
    solution = Solution()
    nums = [5,2,3,1]
    answer = solution.sort_array(nums)
    print(answer)

if __name__ == "__main__":
    main()
             
