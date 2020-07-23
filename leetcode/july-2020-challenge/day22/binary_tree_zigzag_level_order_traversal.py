# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its zigzag level order traversal as:

# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        order = list()
        
        level = [root]
        reverse = False
        while len(level):
            level_order = list()
            next_level = list()
            
            for i in range(len(level) - 1, -1, -1):
                node = level[i]
                
                if node:
                    level_order.append(node.val)
                    
                    if reverse:
                        next_level.append(node.right)
                        next_level.append(node.left)
                    else:
                        next_level.append(node.left)
                        next_level.append(node.right)
            
            if len(level_order):
                order.append(level_order)
            reverse = not reverse
            level = next_level
            
        return order
            