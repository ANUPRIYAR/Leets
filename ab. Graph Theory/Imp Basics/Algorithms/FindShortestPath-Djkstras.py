# User function Template for python3
from typing import List
from collections import defaultdict
import heapq
import math

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:

        # Create adjacency list
        adj = defaultdict(list)
        for edge in edges:
            u, v, dist = edge[0], edge[1], edge[2]
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        # Intialize priority queue
        pq = []

        dist = [math.inf] * (n + 1)   # Create distance list with n + 1 elements coz 1 based indexing
        parent = list(range(n + 1))   # create parent list to store the path

        dist[1] = 0                             # Initialize the source 1 with 0 distance
        heapq.heappush(pq, (dist[1], 1))      # Push the source node to the queue

        while pq:
            prevdist, node = heapq.heappop(pq)

            for neighbours in adj[node]:
                curnode = neighbours[0]
                curdist = neighbours[1]

                if prevdist + curdist < dist[curnode]:      # relax the edge
                    dist[curnode] = prevdist + curdist
                    heapq.heappush(pq, (prevdist + curdist, curnode))
                    parent[curnode] = node                                  # update the parent

        if dist[n] == math.inf:    # If distance to a node could not be found, return an array containing -1.
            return [-1]

        # Iterate backwards from destination to source through parent array
        path = []
        node = n                        # start from the destination node
        while parent[node] != node:    # Until the parent to a node is node itself ie. it is not the source node
            path.append(node)         # append the node to the path
            node = parent[node]       # get the parent of the node as the current node
        path.append(1)                # append the source node to the path

        path.reverse()
        return path

edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
n = 5
m= 6

sol = Solution()
print(sol.shortestPath(n, m, edges))