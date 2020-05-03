# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = [0] * 26
        
        for letter in magazine:
            dictionary[ord(letter) - 97] += 1
            
        for c in ransomNote:
            if dictionary[ord(c) - 97]:
                dictionary[ord(c) - 97] -= 1
            else:
                return False
            
        return True
        