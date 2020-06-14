# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# Input: [1,2,4,8]
# Output: [1,2,4,8]


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        
        sorted_nums = sorted(nums)
        
        largest = 0
        subsets = list()
        for i in range(len(sorted_nums)):
            s = (1, sorted_nums[i], None)
            for j in range(i - 1, -1, -1):
                if sorted_nums[i] % sorted_nums[j] == 0 and subsets[j][0] + 1 > s[0]:
                    s = (subsets[j][0] + 1, sorted_nums[i], j)
                    
            subsets.append(s)
            if s[0] > subsets[largest][0]:
                largest = i
        
        out = list()
        ptr = largest
        while not ptr is None:
            curr = subsets[ptr]
            out.append(curr[1])
            ptr = curr[2]
        return out
