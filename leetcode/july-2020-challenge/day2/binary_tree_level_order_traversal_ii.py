# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its bottom-up level order traversal as:

# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        out = list()
        
        def helper(level):
            order = list()
            next_level = list()
            
            for node in level:
                if node:
                    order.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                    
            if len(next_level):
                helper(next_level)
            
            if len(order):
                out.append(order)
            
        helper([root])
        
        return out
        