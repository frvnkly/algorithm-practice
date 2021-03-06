# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
 

# Constraints:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5


class Solution:    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        classes = [list() for _ in range(numCourses)]
        
        for p in prerequisites:
            classes[p[0]].append(p[1])
        
        done = [0] * numCourses
        for c in range(numCourses):
            stack = [(c, [0] * numCourses)]
            while len(stack) > 0:
                i, path = stack.pop()
                    
                if path[i]:
                    return False                
                path[i] = 1
                
                if done[i]:
                    continue
                done[i] = 1
                
                if len(classes[i]) > 1:
                    for preq in classes[i]:
                        stack.append((preq, path[:]))
                if len(classes[i]) == 1:
                    stack.append((classes[i][0], path))
                
        return True
    