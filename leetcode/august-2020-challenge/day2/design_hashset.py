# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

# Example:

# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)

# Note:

# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.


import math

MAX_ENTRIES = 10000

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = math.ceil(MAX_ENTRIES * 1.3)
        self.buckets = [None] * self.size

    def add(self, key: int) -> None:
        i = key % self.size
        
        if self.buckets[i] is None:
            self.buckets[i] = [key, None]
        else:
            ptr = self.buckets[i]
            while ptr:
                if ptr[0] == key:
                    return
                elif ptr[1] is None:
                    ptr[1] = [key, None]
                else:
                    ptr = ptr[1]

    def remove(self, key: int) -> None:
        i = key % self.size
        
        if self.buckets[i] is None:
            return
        else:
            prev = None
            ptr = self.buckets[i]
            
            while ptr:
                if ptr[0] == key:
                    if prev is None:
                        self.buckets[i] = ptr[1]
                    else:
                        prev[1] = ptr[1]
                    return
                else:
                    prev = ptr
                    ptr = ptr[1]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = key % self.size
        
        ptr = self.buckets[i]
        while ptr:
            if ptr[0] == key:
                return True
            else:
                ptr = ptr[1]
                
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)