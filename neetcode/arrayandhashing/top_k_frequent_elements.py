"""
The logic to find top k frequest items is as follows:
- Firstly create a freuency map that store the frequency of each element in the given array.
- Using this map, can be easily figured that which element has occurences k or more then k.
- To do above step, iterate the map , while iterating check the value is greater or equal to k if yes then store the key in an array.
- Lastly returns the array
"""
from typing import List
class Solution:
    def top_k_frequent_elements(self,nums:List[int], k: int)->List[int]:
        frequency_map = {}
        for element in nums:
            if element in frequency_map:
                frequency_map[element] += 1
            else:
                frequency_map[element] = 1 
        result = []
        for key, val in frequency_map.items():
            if val >= k:
                result.append(key)
        return result

if __name__ =='__main__':
    nums1 =[1,1,1,2,2,3] 
    k1 = 2
    solution = Solution() 
    result = solution.top_k_frequent_elements(nums = nums1,k=k1)
    print(f'top_k_frequent_elements: {result} ')    

    nums2 =[1] 
    k2 = 1
    solution = Solution() 
    result = solution.top_k_frequent_elements(nums = nums2,k=k2)
    print(f'top_k_frequent_elements: {result} ')   

    nums3 =[1,2,2,3] 
    k3 = 2
    solution = Solution() 
    result = solution.top_k_frequent_elements(nums = nums3,k=k3)
    print(f'top_k_frequent_elements: {result} ')   
        
        


