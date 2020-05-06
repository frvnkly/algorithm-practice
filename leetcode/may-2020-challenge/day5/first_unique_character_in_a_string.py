# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqs = dict()
        for c in s:
            freqs.setdefault(c, 0)
            freqs[c] += 1
        
        for i in range(len(s)):
            if freqs[s[i]] == 1:
                return i
        return -1    
