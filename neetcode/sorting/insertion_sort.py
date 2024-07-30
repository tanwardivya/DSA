class Solution:
    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                arr[j+1] = key

def main():
    solution = Solution()
    arr = [40, 30, 20, 10]
    answer = solution.insertion_sort(arr)
    print("sorted array is:", arr)

if __name__ == "__main__":
    main()
