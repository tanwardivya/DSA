from typing import List
class Solution:
    def replace_elements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse the iteration
        # new_max = max(old_max, arr[i])

        right_max = -1
        for i in range(len(arr)-1, -1, -1):
            new_max = max(right_max,arr[i])
            arr[i] = right_max
            right_max = new_max

        return arr

def main():
    solution = Solution()
    arr =  [17,18,5,4,6,1]
    ans = solution.replace_elements(arr)
    print(ans)

if __name__ == "__main__":
    main()

