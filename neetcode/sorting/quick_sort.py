from typing import List
class Solution:
    def quick_sort(self, arr: List[int], start:int, end:int)-> List[int]:
        if start >= end:
            return arr
        pivot = arr[end]
        left = start
        
        for i in range(start, end):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        arr[left], arr[end] = arr[end], arr[left]

        self.quick_sort(arr, start, left-1)
        self.quick_sort(arr, left+1, end)
        return arr
    
def main():
    arr = [6,2,4,1,3]
    solution = Solution()
    sorted_arr = solution.quick_sort(arr,0, len(arr)-1)
    print(f"Sorted array: {sorted_arr}")

if __name__ == "__main__":
    main()
        
        
        