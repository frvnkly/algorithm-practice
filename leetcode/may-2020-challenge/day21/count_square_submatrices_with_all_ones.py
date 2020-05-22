# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
 

# Constraints:

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        num_squares = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    diag = 0 if (i == 0 or j == 0) else matrix[i-1][j-1]
                    up = 0 if i == 0 else matrix[i-1][j]
                    left = 0 if j == 0 else matrix[i][j-1]
                    
                    size = min(diag, up, left)
                    
                    num_squares += size + 1
                    matrix[i][j] = size + 1
                    
        return num_squares
                    