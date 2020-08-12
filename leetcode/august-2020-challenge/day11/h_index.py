# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# Example:

# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.


class Solution:
    def hIndex(self, citations: List[int]) -> int:        
        citations.sort()
        for i in range(len(citations)):
            h = len(citations) - i
            if h <= citations[i]:
                return h
        
        max_h = 0
        left, right = 0, len(citations) - 1
        while left < right:
            mid = (left + right) // 2
            
            h = len(citations) - mid
            if h <= citations[mid]:
                max_h = max(max_h, h)
                right = mid
            else:
                left = right + 1
                
        return max_h
        