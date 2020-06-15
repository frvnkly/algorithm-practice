# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

# Constraints:

# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.


import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        flight_dict = [list() for _ in range(n)]
        for f in flights:
            flight_dict[f[0]].append((f[1], f[2]))
        
        heap = list()
        for x in flight_dict[src]:
            initial_cost, next_stop, initial_stops = x[1], x[0], 0
            heapq.heappush(heap, (initial_cost, next_stop, initial_stops))
        
        while len(heap):
            cost, next_stop, stops = heapq.heappop(heap)
            
            if next_stop == dst:
                return cost
            
            if stops >= K:
                continue
                
            for e in flight_dict[next_stop]:
                heapq.heappush(heap, (cost + e[1], e[0], stops + 1))
            
        return -1
            