# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:



# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Note:

# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque()
        queue.append((root, 0, None))
        
        target_depth = None
        target_parent = None
        
        while len(queue) > 0:
            ptr, depth, parent = queue.popleft()
            if ptr:
                is_target = ptr.val == x or ptr.val == y
                
                if target_depth is None:
                    if is_target:
                        target_depth = depth
                        target_parent = parent
                elif depth == target_depth and is_target:
                    return parent != target_parent
                elif depth > target_depth:
                    break                    

                queue.append((ptr.left, depth + 1, ptr.val))
                queue.append((ptr.right, depth + 1, ptr.val))
        
        return False
    