# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.fill(board, i, 0, 'O', '_')
            if board[i][-1] == 'O':
                self.fill(board, i, len(board[i]) - 1, 'O', '_')
                
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self.fill(board, 0, j, 'O', '_')
            if board[-1][j] == 'O':
                self.fill(board, len(board) - 1, j, 'O', '_')
                
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == '_':
                    board[x][y] = 'O'                    
                elif board[x][y] == 'O':
                    board[x][y] = 'X'
        
        return
    
    def fill(self, board, x, y, a, b):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = [(x, y)]
        while len(stack):
            i, j = stack.pop()
            if board[i][j] == a:
                board[i][j] = b
                
                for d in directions:
                    k = i + d[0]
                    l = j + d[1]
                    if 0 <= k < len(board) and 0 <= l < len(board[i + d[0]]) and board[k][l] == a:
                        stack.append((k, l))        
        