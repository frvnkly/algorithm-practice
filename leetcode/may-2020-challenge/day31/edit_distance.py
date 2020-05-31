# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        edit_distances = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        for x in range(len(word1)):
            edit_distances[x+1][0] = x + 1
        for y in range(len(word2)):
            edit_distances[0][y+1] = y + 1
        
        for i in range(len(word1)):
            for j in range(len(word2)):
                substitution = 0 if word1[i] == word2[j] else 1
                edit_distances[i+1][j+1] = min(
                    edit_distances[i][j+1] + 1,
                    edit_distances[i+1][j] + 1,
                    edit_distances[i][j] + substitution
                )
        
        return edit_distances[-1][-1]
        