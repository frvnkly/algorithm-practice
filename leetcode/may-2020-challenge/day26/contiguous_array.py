# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:

# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:

# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        
        sum_left = list()
        sum_left_dict = dict()
        acc = 0
        for i in range(len(nums)):
            # subarray begins at 0
            if nums[i] == 0:
                acc -= 1
            else:
                acc += 1
            sum_left.append(acc)
            
            if acc == 0:
                max_length = max(max_length, i + 1)
                
            # subarray begins at i
            if sum_left_dict.get(acc) is None:
                sum_left_dict[acc] = i
            else:
                max_length = max(max_length, i - sum_left_dict[acc])
                
        return max_length
    