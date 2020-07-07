# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    return self.get_perimeter(grid, i, j)
        
    def get_perimeter(self, grid, i, j):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        perimeter = 0
        stack = [(i, j)]
        while len(stack):
            x, y = stack.pop()
            
            if grid[x][y] == 1:
                for d in directions:
                    a = x + d[0]
                    b = y + d[1]
                    
                    if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[a]) or grid[a][b] == 0:
                        perimeter += 1
                    else:
                        if grid[a][b] == 1:
                            stack.append((a, b))
                
                grid[x][y] = 2
                
        return perimeter
                                    