from collections import Counter
import heapq
class Solution:
    def frequency_sort(self, s: str) -> str:

        counter = Counter(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        result = ''
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * -freq
        return result

def main():
    solution = Solution()
    s = "tree"
    result = solution.frequency_sort(s)
    print(result)

    s = "cccaaa"
    result = solution.frequency_sort(s)
    print(result)

    s = "Aabb"
    result = solution.frequency_sort(s)
    print(result)

if __name__ == "__main__":
    main()