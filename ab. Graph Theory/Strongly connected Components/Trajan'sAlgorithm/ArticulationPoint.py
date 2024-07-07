"""
Articulation Point : Nodes on whose removal the graph breaks into mulitple components
"""

class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node]= 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0
        for it in adj[node]:
            if it == parent:
                continue
            if not vis[it]:
                self.dfs(it, node, vis, tin, low, mark, adj)
                low[node] = min(low[node], low[it])
                if low[it] >= tin[node] and parent != -1:
                    mark[node]= 1
                child += 1
            else:
                low[node] = min(low[node], low[it])

        if child > 1 and parent == -1:
            mark[node] = 1

    def articulationPoints(self, n, adj):
        vis = [0]*n
        tin = [0]*n
        low = [0]*n
        mark = [0]*n
        for i in range(n):
            if not vis[i]:
                self.dfs(i, -1, vis, tin , low, mark, adj)

        ans = []
        for i in range(n):
            if mark[i] == 1:
                ans.append(i)

        if len(ans) == 0:
            return [-1]
        return ans


n = 5
edges = [[0, 1], [1, 4], [2, 4], [2, 3], [3, 4]]
adj = [[] for _ in range(n)]
for it in edges:
    u, v = it[0], it[1]
    adj[u].append(v)
    adj[v].append(u)
obj = Solution()
nodes = obj.articulationPoints(n, adj)
for node in nodes:
    print(node, end=" ")
print()