import heapq

class Solution:
    def spanningTree(self, V, adj):
        pq = []  # priority queue
        vis = [0]*V  # visited array
        heapq.heappush(pq, (0, 0))  # {wt, node}
        sum = 0
        while pq:
            wt, node = heapq.heappop(pq)
            if vis[node] == 1:
                continue
            vis[node] = 1
            sum += wt
            for it in adj[node]:
                adjNode, edW = it[0], it[1]
                if not vis[adjNode]:
                    heapq.heappush(pq, (edW, adjNode))
        return sum


V = 5
edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
adj = [[] for _ in range(V)]
for it in edges:
    tmp = [it[1], it[2]]
    adj[it[0]].append(tmp)
    tmp = [it[0], it[2]]
    adj[it[1]].append(tmp)

obj = Solution()
sum = obj.spanningTree(V, adj)
print("The sum of all the edge weights:", sum)