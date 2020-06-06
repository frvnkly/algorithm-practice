# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

# Note:

# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:

# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:

# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:

# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.


import random

class Solution:

    def __init__(self, w: List[int]):
        self._range = list()
        
        weights_sum = 0
        for n in w:
            self._range.append((weights_sum, weights_sum + n))
            weights_sum += n

    def pickIndex(self) -> int:        
        target = random.randrange(self._range[-1][1])
        left = 0
        right = len(self._range) - 1
        while left < right:
            mid = (left + right) // 2
            if target < self._range[mid][0]:
                right = mid
            elif target >= self._range[mid][1]:
                left = mid + 1
            else:
                return mid
            
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()