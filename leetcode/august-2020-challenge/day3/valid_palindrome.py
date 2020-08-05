# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false
 
# Constraints:

# s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < len(s) and not s[i].isalnum():
            i += 1
        while j >= 0 and not s[j].isalnum():
            j -= 1
            
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                if s[i].lower() != s[j].lower():
                    return False
            elif s[i] != s[j]:
                    return False
                
            i += 1
            j -= 1
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
        
        return True
        