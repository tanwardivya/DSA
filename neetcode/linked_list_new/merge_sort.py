from typing import List


class Solution:
    def merge_sort(self,arr:List[int], start:int, end:int)-> List[int]:
        if (end - start + 1) <= 1:
            return arr

        mid = (start + end) // 2

        self.merge_sort(arr, start, mid)

        self.merge_sort(arr, mid + 1, end)

        self.merge(arr, start, mid, end)

        return arr

    def merge(self, arr:List[int], start:int, mid:int, end:int)->None:
        Left = arr[start:mid + 1]
        Right = arr[mid + 1 : end + 1]
        i, j, k = 0, 0, start
        while i <len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        while i< len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

def main():
    solution = Solution()
    arr = [3,2,4,1,6]
    sorted_arr = solution.merge_sort(arr, 0, len(arr) - 1)
    print(sorted_arr)

if __name__ == "__main__":
    main()








    
