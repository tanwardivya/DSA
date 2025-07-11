class Solution:
    def majority_element(self, nums):
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n//2:
                return num
            
def main():
    solution = Solution()
    nums = [5,5,1,1,1,5,5]
    print(solution.majority_element(nums))  

if __name__ == "__main__":
    main()