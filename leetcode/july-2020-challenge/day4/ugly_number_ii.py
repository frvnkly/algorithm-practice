# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglys = [1]
        ptr2, ptr3, ptr5 = 0, 0, 0
        for _ in range(n - 1):
            next2 = uglys[ptr2] * 2
            next3 = uglys[ptr3] * 3
            next5 = uglys[ptr5] * 5
            
            if next2 < next3 and next2 < next5:                
                uglys.append(next2)
                ptr2 += 1                                
            elif next3 < next5:
                uglys.append(next3)
                ptr3 += 1
                
                if next2 == next3:
                    ptr2 += 1
            else:
                uglys.append(next5)
                ptr5 += 1
                
                if next2 == next5:
                    ptr2 += 1
                if next3 == next5:
                    ptr3 += 1
        
        return uglys[-1]
            