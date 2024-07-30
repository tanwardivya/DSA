class Solution:
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            smallest = i
            for j in range(i+1, n):
                if arr[j] < arr[smallest]:
                    smallest = j
                    # now dierctly swapping the elements
                    arr[i],arr[smallest] = arr[smallest], arr[i]

def main():
    solution = Solution()
    arr = [24, 41, 33, 42, 17]
    answer = solution.selection_sort(arr)
    print("Sorted array after selection sort is:", arr)


if __name__ == "__main__":
    main()