# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
    
        triplets = set()
    
        for x in range(len(sorted_nums) - 2):
            y = x + 1
            z = len(sorted_nums) - 1
            
            while y < z:
                a, b, c = sorted_nums[x], sorted_nums[y], sorted_nums[z]
                s = a + b + c
                    
                if s > 0:
                    z -= 1
                elif s < 0:
                    y += 1
                else:
                    triplets.add((a, b, c))
                    y += 1
                    z -= 1
                    
        return triplets
                    