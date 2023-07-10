from typing import List, Tuple

class Solution:

    def longest_consecutive_string(self, nums:List[int])-> Tuple[int, List[int]]:
        num_set = set(nums)
        longest = 0
        max_sequence = []
        
        for n in nums:
            if(n-1) not in num_set:
                length = 0
                sequence = []
                sequence.append(n)
                while (n + length) in num_set:
                    length += 1
                    if (n + length) in num_set:
                        sequence.append(n+length)
                longest = max(length , longest)
                max_sequence = sequence if len(sequence) > len(max_sequence) else max_sequence
        return longest, max_sequence

if __name__ == '__main__':
        input1 = [100,4,200,1,3,2]
        solution = Solution()
        result, max_sequence = solution.longest_consecutive_string(nums = input1)
        print(f'Length of longest consecutive sequence:{result}')
        print(f'Longest Max sequence:{max_sequence}')