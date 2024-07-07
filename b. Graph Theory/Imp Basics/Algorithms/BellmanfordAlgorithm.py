import sys

class Solution:
    def bellman_ford(self, V, edges, S):
        dist = [sys.maxsize] * V
        dist[S] = 0
        for _ in range(V - 1):
            for it in edges:
                u, v, wt = it[0], it[1], it[2]
                if dist[u] != sys.maxsize and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        # Nth relaxation to check negative cycle
        for it in edges:
            u, v, wt = it[0], it[1], it[2]
            if dist[u] != sys.maxsize and dist[u] + wt < dist[v]:
                return [-1]

        return dist


V = 6
edges = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]
S = 0
obj = Solution()
dist = obj.bellman_ford(V, edges, S)
for d in dist:
    print(d, end=" ")
print()