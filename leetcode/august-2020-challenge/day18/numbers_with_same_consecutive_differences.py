# Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

# Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

# You may return the answer in any order. 

# Example 1:

# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# Example 2:

# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 
# Note:

# 1 <= N <= 9
# 0 <= K <= 9


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        out = list()
        
        stack = list()
        for n in range(1, 10):
            stack.append([n])
        if N == 1:
            stack.append([0])
            
        while len(stack):
            num = stack.pop()
            
            if len(num) == N:
                out.append(''.join(map(str, num)))
                continue
                
            minus = num[-1] - K
            plus = num[-1] + K
            if minus == plus:
                num.append(minus)
                stack.append(num)
            elif minus >= 0 and plus <= 9:
                stack.append(num + [minus])
                num.append(plus)
                stack.append(num)
            elif minus >= 0:
                num.append(minus)
                stack.append(num)
            elif plus <= 9:
                num.append(plus)
                stack.append(num)
                
        return out                
        