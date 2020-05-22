# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input:
# "cccaaa"

# Output:
# "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"

# Output:
# "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 0:
            return ''
        
        count = Counter(s)
        longest = count.most_common(1)[0][1]
        
        buckets = [list() for _ in range(longest + 1)]
        for c in count:
            buckets[count[c]].append(c)
            
        out = list()
        for i in range(len(buckets) - 1, -1, -1):
            for c in buckets[i]:
                out.append(c*i)
        return ''.join(out)
        