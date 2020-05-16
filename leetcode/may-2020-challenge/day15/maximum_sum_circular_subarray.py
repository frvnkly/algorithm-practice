# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

# Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

# Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

# Example 1:

# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
# Example 2:

# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
# Example 3:

# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
# Example 4:

# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
# Example 5:

# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
 

# Note:

# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000


import math

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_contiguous_sum = -math.inf
        current_contiguous_sum = 0
        
        max_element = -math.inf
        
        max_wrap_sum = -math.inf
        wrap_sum_right = [None] * len(A)
        wrap_right_acc = 0
        wrap_right_max_so_far = 0
        
        for i in range(len(A)):
            # Kadane's
            current_contiguous_sum = max(0, current_contiguous_sum + A[i])
            max_contiguous_sum = max(max_contiguous_sum, current_contiguous_sum)
            
            max_element = max(max_element, A[i])
            
            # calculate max so far of right side of wrap sum
            wrap_right_acc += A[i]
            wrap_right_max_so_far = max(wrap_right_max_so_far, wrap_right_acc)
            wrap_sum_right[i] = wrap_right_max_so_far
        
        # iterate list backwards to calculate left side of wrap sum and max split sum
        wrap_left_acc = 0
        wrap_left_max_so_far = 0
        for j in range(len(A) - 1, -1, -1):
            max_wrap_sum = max(max_wrap_sum, wrap_sum_right[j] + wrap_left_max_so_far)
            wrap_left_acc += A[j]
            wrap_left_max_so_far = max(wrap_left_max_so_far, wrap_left_acc)            
        
        if not max_contiguous_sum and not max_wrap_sum:
            return max_element
        
        return max(max_contiguous_sum, max_wrap_sum)
        