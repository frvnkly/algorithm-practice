# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:                
        anagrams = list()
        target = dict()
        for c in p:
            target.setdefault(c, 0)
            target[c] += 1
            
        substring = dict()
        start = 0
        for i in range(len(s)):
            if target.get(s[i]):
                substring.setdefault(s[i], 0)
                substring[s[i]] += 1
                
                while substring[s[i]] > target[s[i]]:
                    substring[s[start]] -= 1
                    start += 1
                
                if i - start + 1 == len(p):
                    anagrams.append(start)
                    substring[s[start]] -= 1
                    start += 1
            else:
                substring = dict()
                start = i + 1
        
        return anagrams
        