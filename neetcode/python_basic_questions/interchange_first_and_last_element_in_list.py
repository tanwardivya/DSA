# Python3 program to swap first
# and last element of a list
from typing import List
class Solution:
    # Swap function
    def Swap(self, list:List[int])-> List[int]:
        #keep the original list as it is and copy it to another list
        new_list = list[:]
#Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.


  
     #  #get the size of the list
        # size = len(new_list)

        # #swapping first and last element
        # temp = new_list[0]
        # new_list[0] = new_list[size - 1]
        # new_list[size - 1] = temp #


#Approach #2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1]. TC: O(1), SC: O(n), where n is length of list
        #new_list[0],new_list[-1] = new_list[-1],new_list[0]

#Approach #3: Swap the first and last element is using tuple variable. 
# Store the first and last element as a pair in a tuple variable, say 
# get, and unpack those elements with first and last element in that 
# list. Now, the First and last values in that list are swapped. 
        # Storing the first and last element 
        # as a pair in a tuple variable get

        # get = new_list[-1],new_list[0]
        # # Unpacking the tuple and swapping first and last element
        # new_list[0],new_list[-1] =get

#Approach #4: Using * operand. 
#This operand proposes a change to iterable unpacking syntax, allowing 
# to specify a “catch-all” name which will be assigned a list of all 
# items not assigned to a “regular” name. 

        # start, *middle, end = new_list
        # new_list = [end, *middle , start]

#Approach #5: Swap the first and last elements is to use the inbuilt 
# function list.pop(). Pop the first element and store it in a variable.
# Similarly, pop the last element and store it in another variable. Now 
# insert the two popped element at each other’s original position. 

        # pop the first,last element
        # first = new_list.pop(0)#Removes and stores the first element of the list
        # last = new_list.pop(-1)#Removes and stores the last element of the list. 

        # # insert the first and last element at each other's original position
        # new_list.insert(0,last) #0 is the position where the element you want to insert and last is the element you want to insert.
        # new_list.append(first)#Adds the first element to the end of the list.

#Approach #6: Using slicing,  Time Complexity: O(1), Space Complexity: O(1)
        # check if list has atleast 2 elements
        if len(new_list) >= 2:
                #swap the first and last elements using slicing
                new_list = new_list[-1:] + new_list[1:-1] + new_list[:1]

        return new_list
 
        
def main():
    solution = Solution()
    list = [12, 35, 9, 56, 24]
    result = solution.Swap(list)
    print("Original List:", list)
    print("Original List:", result)

if __name__ == "__main__":
    main()



