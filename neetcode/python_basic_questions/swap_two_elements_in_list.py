from typing import List
class Solution:
#Approach1: Swap Two Elements in a List using comma assignment 
#Time Complexity: O(1), for using constant operations, Auxiliary Space: O(1), for using constant extra space.
    # def swap_positions(self, list:List[int], pos1:int, pos2:int)-> List[int]:
    #     new_list = list[:]
    #     new_list[pos1], new_list[pos2] = new_list[pos2], new_list[pos1]
    #     return new_list


# Approach2: Using Inbuilt list.pop() function to Swap Two Elements in a List

    # def swap_positions(self, list:List[int], pos1:int, pos2:int)-> List[int]:
    #     #popping both both elements from the list
    #     first_element = list.pop(pos1)
    #     # The reason for using pos2-1 is that after removing the first element (first_ele), all subsequent elements in the list are shifted one position to the left.
    #     second_element = list.pop(pos2-1)

    #     # inserting the popped elements in their respective positions
    #     list.insert(pos1,second_element)
    #     list.insert(pos2,first_element)
    #     return list

#approach 3: Swap Two Elements in a List Using tuple variable

    # def swap_positions(self, list:List[int], pos1:int, pos2:int)-> List[int]:
    #     #storing the two elements as a pair in a tuple variable get
    #     get = list[pos1], list[pos2]
    #     # unpacking the tuple and swapping the elements
    #     list[pos2],list[pos1] = get
    #     return list

#Approach 4: Swap Two Elements in a List Using temp variable

    # def swap_positions(self, list:List[int], pos1:int, pos2:int)-> List[int]:

    #     #swap function
    #     temp = list[pos1]
    #     list[pos1] = list[pos2]
    #     list[pos2] =temp
    #     return list

#Approach 5: Swap Two Elements in a List Using enumerate tc: O(n), since it involves looping through the entire list to find the elements to be swapped. The space complexity is O(1), since it only uses a constant amount of additional space to store the elements to be swapped.
    def swap_positions(self, list:List[int], pos1:int, pos2:int)-> List[int]:
        for i , x in enumerate(list):
            if i == pos1:
                element1 = x
            if i == pos2:
                element2 = x

        
        list[pos1] = element2
        list[pos2] = element1
        return list

        




def main():
    solution = Solution()
    list = [23, 65, 19, 90]
    pos1 = 1
    pos2 = 3 
    result = solution.swap_positions(list, pos1-1, pos2-1) #if the input indexes are not strating from 0th index, subtract 1 from the input
    print(result)



if __name__ == "__main__":
    main()