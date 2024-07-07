class DisjointSet:
    def __init__(self, n):
        self.rank = [0]* (n+1)
        self.parent = list(range(n+1))
        self.size = [0]*(n+1)

    def findUltPar(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUltPar(self.parent[node])
        return self.parent[node]

    def UnionByRank(self, u, v):
        ult_u = self.findUltPar(u)
        ult_v = self.findUltPar(v)
        if ult_u  == ult_v:
            return

        if self.rank[ult_u] > self.rank[ult_v]:
            self.parent[ult_v] = ult_u
        elif self.rank[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        else:
            self.parent[ult_v] = ult_u
            self.rank[ult_u] += 1

    def UnionBySize(self, u, v):
        ult_u = self.findUltPar(u)
        ult_v = self.findUltPar(v)
        if ult_u == ult_v:
            return

        if self.size[ult_u] < self.size[ult_v]:
            self.parent[ult_u] = ult_v
            self.size[ult_v] += self.size[ult_u]
        else:
            self.parent[ult_v] = ult_u
            self.size[ult_u] += self.size[ult_v]

class Solution:
    def spanningTree(self, V, adj):
        edges = []
        for i in range(V):     # Create edges
            for it in adj[i]:
                adjnode, wt = it[0], it[1]
                node = i
                edges.append((wt, (node, adjnode)))

        ds = DisjointSet(V)    # Initialize DisjointSet object instance

        edges.sort()            # Sort the edges by weight  ==> important step

        min_span_tree_wt = 0
        for it in edges:
            wt, nodes = it[0], it[1]   # get current weight and nodes u, v
            u, v = nodes[0], nodes[1]

            if ds.findUltPar(u) != ds.findUltPar(v):  # check if ultimate parent of current node is not same as other
                min_span_tree_wt += wt          # then add up the current weight for min spanning tree weight
                ds.UnionBySize(u, v)          # do union of u and v by size
        return min_span_tree_wt





