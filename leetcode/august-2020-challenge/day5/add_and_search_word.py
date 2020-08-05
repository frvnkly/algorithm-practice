# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)

# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# Example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true

# Note:
# You may assume that all words are consist of lowercase letters a-z.


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        ptr = self.trie
        for l in word:
            c = ord(l) - ord('a')
            if not ptr.children[c]:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.trie, 0)]        
        while len(stack):
            ptr, i = stack.pop()
            
            if i == len(word):
                if ptr.is_word:
                    return True
            elif word[i] == '.':
                for child in ptr.children:
                    if child:
                        stack.append((child, i+1))
            else:
                c = ord(word[i]) - ord('a')
                if ptr.children[c]:
                    stack.append((ptr.children[c], i+1))
                    
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
