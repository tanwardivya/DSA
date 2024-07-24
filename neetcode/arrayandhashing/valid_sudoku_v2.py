from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #The line rows = collection.defaultdict(set) creates a dictionary called rows where each 
        #key automatically has a default value of an empty set if the key does not exist when 
        #accessed. This can be very useful when you want to group elements together without having
        #to check if the key already exists in the dictionary before adding an element to the set.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

            return True
