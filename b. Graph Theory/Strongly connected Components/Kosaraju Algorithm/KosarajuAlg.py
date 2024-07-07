class Solution:
    def dfs(self, node, vis, adj, stack):
        vis[node] = 1
        for it in adj[node]:
            self.dfs(it, vis, adj, stack)
        stack.append(node)

    def dfs3(self, node, vis, adjT):
        vis[node] = 1
        for it in adjT[node]:
            if not vis[it]:
                dfs3(self, it, vis, adjT)

    def kosaraju(self, V, adj):
        vis = [0]*V
        stack  = []

        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, vis, adj, stack)

        adjT = [[] for _ in range(V)]
        for i in range(V):
            vis[i] = 0
            for it in adj[i]:
                adj[it].append(i)


        scc = 0
        while stack:
            node = stack.pop()
            if not vis[node]:
                scc += 1
                self.dfs3(node, vis, adjT)

        return scc