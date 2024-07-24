from typing import List
class Solution:
    def number_of_islands(self,grid:List[List[str]])->int:
        m = len(grid)
        n = len(grid[0])
        total_count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid, m, n)
                    total_count += 1
        return total_count

    
    
    def dfs(self,row:int,col:int,grid:List[List[str]],m:int,n:int)->None:
        if row>=0 and row < m and col >= 0 and col < n and grid[row][col]!= '0' and grid[row][col]!='T':
            grid[row][col] = 'T'

            self.dfs(row + 1, col, grid, m, n)
            self.dfs(row - 1, col, grid, m, n)
            self.dfs(row, col + 1, grid, m, n)
            self.dfs(row, col - 1, grid, m, n)


