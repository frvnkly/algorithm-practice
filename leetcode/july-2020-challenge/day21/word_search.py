# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
 
# Constraints:

# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.search_for_word(board, i, j, word):
                    return True
                
        return False
        
    def search_for_word(self, board, i, j, word):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        stack = [(i, j, set(), 0)]
        while len(stack):
            x, y, path, c = stack.pop()            
            
            if board[x][y] == word[c]:
                if c >= len(word) - 1:
                    return True
                
                path.add((x, y))
                
                for d in directions:
                    a = x + d[0]
                    b = y + d[1]

                    if a >= 0 and a < len(board) and b >= 0 and b < len(board[a]) and (a, b) not in path:
                        stack.append((a, b, path.copy(), c + 1))
                        
        return False
    