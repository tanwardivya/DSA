from typing import List
class Solution:
    def concatenation_of_array(self,nums:List[int])->List[int]:

        # res = []
        # for i in range(2):
        #     for n in nums:
        #         res.append(n)

        # return res
        n = len(nums)
        res = [0] * (2*n)
        for i, num in enumerate(nums):
            res[i]= res[i+n] = num
        return res

def main():
    solution = Solution()
    nums = [1,2,3]
    ans = solution.concatenation_of_array(nums)
    print(ans)
    
if __name__ == "__main__":
    main()