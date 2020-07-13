# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_stack = [p]
        q_stack = [q]
        
        while len(p_stack) and len(q_stack):
            a = p_stack.pop()
            b = q_stack.pop()
            
            if a and b:
                if a.val == b.val:
                    p_stack.append(a.left)
                    p_stack.append(a.right)
                    q_stack.append(b.left)
                    q_stack.append(b.right)
                else:
                    return False
            elif a or b:
                return False
            
        return len(p_stack) == len(q_stack)                
    