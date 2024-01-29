"""This module containe how to check duplicate in an array."""
from typing import List
class Solution:
    """Solution class for checking duplicate number."""

    def contains_duplicate(self, array:List[int]) -> bool:
        """Check for duplicate element in an array.

        Args:
            array (List): List of integers

        Returns:
            bool: Return true if it contains duplicate otherwise returns false
        """
        for index1 in range(0, len(array)):
            for index2 in range(1,len(array)):
                if array[index2] == array[index1]:
                    return True
        return False   

    def contains_duplicate_v2(self, array:List[int])->bool:
        """_summary_

        Args:
            array (List): _description_

        Returns:
            bool: _description_
        """
        array = sorted(array)# the input array sorted using the sorted function 
        temp = array[0]#the variable temp is initialised with the first element of the sorted array
        for index in range(1,len(array)):
            if array[index] == temp:
                return True
            temp =  array[index]   
        return False

    def contains_duplicate_v3(self, array: List[int]) -> bool:
        """_summary_

        Args:
            array (List[int]): _description_

        Returns:
            bool: _description_
        """
        hashset = set()
        for element in array:
            if element in hashset:
                return True
            hashset.add(element)
        return False

if __name__ == '__main__':
    solution = Solution()
    input_array = [5,1,3,4,2,1,5]
    result = solution.contains_duplicate(input_array)
    print(f'Contains Duplicate: {result}')
    input_array = [8,4,3,6,9,3]
    result = solution.contains_duplicate(input_array)
    print(f'Contains Duplicate: {result}')
    input_array = [8,4,3,6,9,3]
    result = solution.contains_duplicate_v2(input_array)
    print(f'Contains Duplicate: {result}')
    input_array = [8,4,3,6,9,7]
    result = solution.contains_duplicate_v2(input_array)
    print(f'Contains Duplicate: {result}')
    input_array = [8,4,3,6,9,3]
    result = solution.contains_duplicate_v3(input_array)
    print(f'Contains Duplicate: {result}')
    input_array = [8,4,3,6,9,7]
    result = solution.contains_duplicate_v3(input_array)
    print(f'Contains Duplicate: {result}')
    