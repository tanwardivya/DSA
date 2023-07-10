from typing import List
class Solution:
    def valid_sudoku(self, board:List[List[str]])-> bool:
        return(self.is_row_valid(board) and  
               self.is_col_valid(board) and 
               self.is_square_valid(board))

    def is_row_valid(self,board):
        for row in board:  
            if not self.is_cell_valid(row):
                return False
        return True

    def is_col_valid(self,board):
        for col in zip(*board):
            if not self.is_cell_valid(col):
                return False
        return True

    def is_square_valid(self,board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range (j, j + 3)]
                if not self.is_cell_valid(square):
                    return False
        return True

    def is_cell_valid(self, cell):
        cell= [i for i in cell if i != '.']
        return len(set(cell)) == len(cell)

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    result = solution.valid_sudoku(board=board)
    print(f'Is Valid Sudoku:{result}')
