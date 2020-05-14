# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.


class Trie:
    
    class Node:
        def __init__(self, val):
            self.val = val
            self.children = list()
            self.is_word = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = self.Node('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self._root
        for c in word:
            exists = False
            for n in ptr.children:
                if n.val == c:
                    ptr = n
                    exists = True
                    break
            
            if not exists:
                new = self.Node(c)
                ptr.children.append(new)
                ptr = new
        ptr.is_word = True
        return
                    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self._root
        for c in word:
            exists = False
            for n in ptr.children:
                if n.val == c:
                    ptr = n
                    exists = True
                    break
            
            if not exists:
                return False
        return ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self._root
        for c in prefix:
            exists = False
            for n in ptr.children:
                if n.val == c:
                    ptr = n
                    exists = True
                    break
            
            if not exists:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
