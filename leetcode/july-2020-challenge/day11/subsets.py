# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = list()
    
        stack = [([], 0)]
        end = len(nums) - 1
        while len(stack):
            subset, i = stack.pop()
            
            subset_copy = subset[:]
            subset_copy.append(nums[i])
            
            if i == end:
                subsets.append(subset)
                subsets.append(subset_copy)
            else:
                stack.append((subset, i+1))
                stack.append((subset_copy, i+1))
                
        return subsets
                