# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

# Example 1:

# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        stack = list()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    for d in directions:
                        stack.append((i + d[0], j + d[1], 1))
                    
        minutes_to_rot = dict()
        while len(stack):
            a, b, minutes = stack.pop()
            
            if a >= 0 and a < len(grid) and b >= 0 and b < len(grid[a]):
                if grid[a][b] == 1:
                    if minutes_to_rot.get((a, b)) is None or minutes < minutes_to_rot[(a, b)]:
                        minutes_to_rot[(a, b)] = minutes
                        
                        for d in directions:
                            stack.append((a + d[0], b + d[1], minutes + 1))
        
        minutes_to_rot_board = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    if minutes_to_rot.get((x, y)):
                        minutes_to_rot_board = max(minutes_to_rot_board, minutes_to_rot[(x, y)])
                    else:
                        return -1
                    
        return minutes_to_rot_board
                        