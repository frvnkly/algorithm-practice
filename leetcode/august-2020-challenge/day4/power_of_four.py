# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfFour(self, num: int) -> bool:        
        power_of_four_mask = 1431655765 # 1010101010101010101010101010101
        
        if num > 0:        
            first_set_bit = num & -num
            if num == first_set_bit:
                if num & power_of_four_mask:
                    return True
            
        return False
        