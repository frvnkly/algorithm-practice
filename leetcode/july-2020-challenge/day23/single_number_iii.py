# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

# Example:

# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:

# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # get the xor of the two once-appearing numbers
        x = reduce(lambda a, b: a ^ b, nums)
            
        # get the first bit differing between the answers
        first_bit = x & -x
        
        # determine one of the answers by xor'ing only the numbers that share the differing bit
        answer1 = reduce(lambda a, b: a ^ b, filter(lambda x: x & first_bit, nums))
        
        # determine the second answer by xor'ing the result of xor'ing all numbers with the first answer
        answer2 = x ^ answer1
        
        return [answer1, answer2]
        