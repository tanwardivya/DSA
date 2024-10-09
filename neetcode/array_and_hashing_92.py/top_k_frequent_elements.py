from typing import List
class Solution:
    def top_k_frequent_elements(self,nums:List[int], k:int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res

def main():
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k= 2
    ans = solution.top_k_frequent_elements(nums, k)
    print(ans)

if __name__ == "__main__":
    main()
