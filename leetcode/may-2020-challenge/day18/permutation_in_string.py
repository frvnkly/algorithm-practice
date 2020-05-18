# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 

# Note:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        for c in s1:
            target[ord(c) - ord('a')] += 1
            
        substring = [0] * 26
        start = 0
        for i in range(len(s2)):
            j = ord(s2[i]) - ord('a')
            if target[j]:
                substring[j] += 1
                
                while substring[j] > target[j]:
                    substring[ord(s2[start]) - ord('a')] -= 1
                    start += 1
                
                if i - start + 1 == len(s1):
                    return True
            else:
                substring = [0] * 26
                start = i + 1
        
        return False
        