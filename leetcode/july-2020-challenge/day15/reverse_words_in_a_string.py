# Given an input string, reverse the string word by word.

# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
# Note:

# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
 
# Follow up:

# For C programmers, try to solve it in-place in O(1) extra space.


class Solution:
    def reverseWords(self, s: str) -> str:
        out = list()
        indices = list()
        
        is_word = False
        word = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if is_word:
                    word[0] = i + 1
                    indices.append(word)
                    word = []
                is_word = False
            else:
                if not is_word:
                    word = [None, i]
                    is_word = True
        if len(word):
            indices.append(word)
        
        for x in indices:
            w = s[x[0]:x[1]+1]            
            out.append(w)
            
        return ' '.join(out)
            