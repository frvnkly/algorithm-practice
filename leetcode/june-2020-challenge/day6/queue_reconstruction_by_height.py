# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

 
# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_by_h = sorted(people, key=lambda x: x[0])
        out = [None] * len(people)
        
        for i in range(len(sorted_by_h)):
            curr = sorted_by_h[i]
            
            j = 0
            larger = curr[1]
            while larger > 0:
                if out[j] is None or out[j][0] == curr[0]:
                    larger -= 1
                j += 1
            
            while out[j]:
                j += 1
                
            out[j] = curr
            
        return out
            