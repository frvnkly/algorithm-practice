# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        
        if num == 0 or num == 1:
            return True
        
        left = 2
        right = num // 2
        while left < right:
            n = left + ((right - left) // 2)
                      
            if n * n < num:
                left = n + 1
            elif n * n > num:
                right = n
            else:
                return True
            
        n = left
        return n * n == num
        