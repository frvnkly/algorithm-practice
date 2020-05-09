# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


# Example 1:

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:

# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
 

# Constraints:

# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # straight vertical line
        if coordinates[0][0] == coordinates[1][0]:
            x = coordinates[0][0]
            return all(map(lambda c: c[0] == x, coordinates))
        
        # straight horizontal line
        if coordinates[0][1] == coordinates[1][1]:
            y = coordinates[0][1]
            return all(map(lambda c: c[1] == y, coordinates))
        
        if coordinates[0][0] < coordinates[1][0]:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        else:
            slope = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        
        for i in range(0, len(coordinates) - 1):
            n, m = coordinates[i], coordinates[i+1]
            try:
                if n[0] < m[0]:
                    s = (m[1] - n[1]) / (m[0] - n[0])
                else:
                    s = (n[1] - m[1]) / (n[0] - m[0])
                if s != slope:
                    return False
            except:
                return False            
        return True
        