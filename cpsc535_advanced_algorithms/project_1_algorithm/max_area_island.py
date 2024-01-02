from typing import List
from collections import deque

class Point:
    """Point."""

    def __init__(self, x:int, y:int) -> None:
        """Point intialization.

        Args:
            x (int): row
            y (int): column
        """
        self.x = x
        self.y = y

class Solution:
    """Design  an algorithm to return the max area of island."""

    def find_max_area_island(self, grid: List[List[int]])-> int:
        """Max area of Island. Calculates the size of the largest possible landmass after changing exactly one 1 to a 0.

        Args:
            grid (List[List[int]]): Grid is a 2D array

        Returns:
            int: Returns max area of island
        """
        max_area = 0
        queue = deque()
        # Add all 1's position into queue
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append(Point(i, j))
        while queue:
            point = queue.popleft() # Poll from the queue
            grid_copy = [row[:] for row in grid] # Make a copy of grid to update water to the land
            # Update water to the land, atmost 1's can be turned to 0
            grid_copy[point.x][point.y] = 0
            #Update max_area after calculating area by changing  available water to land one at a time.
            max_area = max(max_area, self.max_area_island(grid_copy))
        return max_area


    def max_area_island(self, grid:List[List[int]]) -> int:
        """Calculate max area of a island.

        Args:
            grid (List[List[int]]): Grid Is a 2D array

        Returns:
            int: Returns max_area
        """
        max_area = 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                # Max area for a given position(i, j) in the grid
                max_area = max(max_area, self.dfs(grid,i,j))
        return max_area
    
    def dfs(self, grid: List[List[int]], i:int, j:int) -> int:
        """Perform Depth First Search.

        Args:
            grid (List[List[int]]): Grid is a 2D array
            i (int): Position of i
            j (int): Position of j

        Returns:
            int: Area of island from position i and j
        """
        # Check the after changing the direction, position are within grid boundary and 
        # perform depth first search on only land
        if i>=0 and i< (len(grid)) and j>=0 and j<(len(grid)) and grid[i][j]==0:
            grid[i][j] = 1 # Mark as visited
            # Perform DFS in up, down, left and right
            return 1 + self.dfs(grid, i+1, j) + self.dfs(grid,i-1,j)+ self.dfs(grid,i,j-1) + self. dfs(grid, i,j+1)
        return 0

if __name__ == '__main__':
    grid = [[0,1,1], [0,0,1], [1,1,0]]
    solution = Solution()
    print(solution.find_max_area_island(grid))

    grid = [[1,0,1,0,0],[0,0,1,1,0],[0,1,1,1,1],[1,0,1,0,0]]
    print(solution.find_max_area_island(grid))

            
        