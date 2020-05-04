# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

# Example 1:

# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

# Example 2:

# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

# Note:

# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/


class Solution:
    def to_binary(self, n: int) -> str:
        p = 32
        out = list()
        while p >= 0:
            x = 2**p
            if x <= n:
                out.append('1')
                n -= x
            elif len(out) > 0:
                out.append('0')
            p -= 1
        return ''.join(out)
    
    def find_binary_complement(self, binary: str) -> str:
        binary_complement = list()
        for c in binary:
            if c == '1':
                binary_complement.append('0')
            else:
                binary_complement.append('1')
        return ''.join(binary_complement)
    
    def to_base_ten(self, binary: str) -> int:
        out = 0
        p = 0
        for i in range(len(binary) - 1, -1, -1):
            if binary[i] == '1':
                out += 2**p
            p += 1
        return out
    
    def findComplement(self, num: int) -> int:
        binary_num = self.to_binary(num)        
        binary_complement = self.find_binary_complement(binary_num)        
        complement = self.to_base_ten(binary_complement)
        return complement        
