from typing import List
class Solution:
    def search_2d_matrix(self, matrix:List[List[int]], target:int)->bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROWS -1
        while top <= bottom:
            row = (top + bottom) // 2 # to find the mid row
            if target > matrix[row][-1]: #
                 top = row + 1
            elif target < matrix[row][0]: 
                bottom = row -1  
            else:
                break

        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            if target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False

def main():
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
    target = 3
    result = solution.search_2d_matrix(matrix, target)
    print(result)

    matrix = [[1]]
    target = 1
    result = solution.search_2d_matrix(matrix, target)
    print(result)

if __name__ == "__main__":
    main()


# target value is 3.

# Initialization
# ROWS = 3 (since there are 3 lists within the matrix)
# COLS = 4 (since each list contains 4 elements)
# top = 0
# bottom = 2 (ROWS - 1)
# First While Loop (Binary Search on Rows)
# The goal of this loop is to find the row that could contain the target value.

# First Iteration:

# row = (0 + 2) // 2 = 1
# The last element of row 1 (matrix[1][-1]) is 20.
# The first element of row 1 (matrix[1][0]) is 10.
# Since target (3) is less than matrix[1][0] (10), we adjust bottom to row - 1, which is 0.
# The values of interest are matrix[row][-1] = 20 and matrix[row][0] = 10.
# Second Iteration:

# Now, top = 0 and bottom = 0, so row = (0 + 0) // 2 = 0.
# The loop checks if the target is in the first row by comparing it to the first and last elements of the row.
# Since target (3) is between matrix[0][0] (1) and matrix[0][-1] (7), the loop breaks out to proceed with column search in the identified row.
# The values of interest for this iteration are not explicitly printed, but they would be matrix[row][-1] = 7 and matrix[row][0] = 1.
# Second While Loop (Binary Search on Columns within the Identified Row)
# Now, we know the target must be in row 0 if it's present at all. We perform a binary search on this row.

# Initialization for Column Search:

# row is confirmed as 0 from the previous steps.
# left = 0
# right = 3 (COLS - 1)
# First Iteration:

# mid = (0 + 3) // 2 = 1
# target (3) is equal to matrix[0][1] (3), so the function returns True.
# Conclusion
# The program correctly identifies that the target value 3 is present in the matrix and returns True. The key values of matrix[row][-1] and matrix[row][0] during the row binary search were 20 and 10 for the first iteration, indicating the program's logic to narrow down the search row based on the target's comparison with the start and end of each row.





