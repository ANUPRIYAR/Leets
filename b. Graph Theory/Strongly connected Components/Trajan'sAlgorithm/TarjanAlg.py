class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        vis[node]= 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        print(f"Before tin[node] : {tin[node]}  ,low[node] : {low[node]} ,self.timer:{self.timer} ")
        for it in adj[node]:
            if it == parent:
                continue
            if vis[it] == 0:
                self.dfs(it, node, vis, adj, tin, low, bridges)
                print(f"low[node]: {low[node]},low[it] : {low[it]} ")
                low[node] = min(low[it], low[node])
                
                if low[it] > tin[node]:
                    bridges.append([it, node])
            else:
                low[node] = min(low[node], low[it])

    def criticalConnections(self, n, connections):
        adj = [[] for _ in range(n)]

        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0]* n
        tin = [0]* n
        low = [0]* n
        bridges = []
        self.dfs(0, -1, vis, adj, tin, low, bridges)
        return bridges

n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
obj = Solution()
bridges = obj.criticalConnections(n, connections)
for it in bridges:
    print("[", it[0], ", ", it[1], "] ", end="")
print()