from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


def main():
    soloution = Solution()
    piles = [1,4,3,2]
    h = 9
    answer = soloution.minEatingSpeed(piles,h)

if __name__ == "__main__":
    main()
