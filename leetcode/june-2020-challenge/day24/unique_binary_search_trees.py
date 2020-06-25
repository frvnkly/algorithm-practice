# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution:
    def numTrees(self, n: int) -> int:
        memo = {0: 1, 1: 1}
        
        for m in range(2, n + 1):
            num_structures = 0
            for i in range(1, (m // 2) + 1):
                left = memo[i - 1]
                right = memo[m - i]
                num_structures += left * right
            num_structures *= 2
            
            if m % 2 == 1:
                num_structures += memo[m // 2] * memo[m // 2]
        
            memo[m] = num_structures

        return memo[n]
                