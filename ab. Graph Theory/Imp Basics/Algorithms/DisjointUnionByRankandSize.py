class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n+1))
        self.size = [0]* (n + 1)

    def findUltPar(self, node):
        if node == self.parent[node]:     # if parent of node is node itself (i.e. its already ultimate parent), then return node
            return node
        self.parent[node] = self.findUltPar(self.parent[node])   # else find the ultimate parent and store in parent list
        return self.parent[node]

    def UnionByRank(self, u, v):
        if self.findUltPar(u) == self.findUltPar(v):  # If Both u and v belong to same parents, just return
            return
        ultu, ultv = self.findUltPar(u), self.findUltPar(v)

        if self.rank[ultu] < self.rank[ultv]:     # else if rank of u more than v, then u becomes parent of v or viceversa
            self.parent[ultu] = ultv
        elif self.rank[ultu] > self.rank[ultv]:
            self.parent[ultv] = ultu
        else:
            self.parent[ultv] = ultu   # but if rank of u and v are same, then u becomes parent of v
            self.rank[ultu] += 1      # and we increase rank of u by 1

    def UnionBySize(self, u, v):
        ultu, ultv = self.findUltPar(u), self.findUltPar(v)
        if ultu == ultv:
            return

        if self.size[ultu] < self.size[ultv]:
            self.parent[ultv] = ultu
            self.size[ultv] += self.size[ultu]
        else:
            self.parent[ultv] = ultu
            self.size[ultu] += self.size[ultv]


ds = DisjointSet(7)
ds.UnionBySize(1, 2)
ds.UnionBySize(2, 3)
ds.UnionBySize(4, 5)
ds.UnionBySize(6, 7)
ds.UnionBySize(5, 6)

if ds.findUltPar(3) == ds.findUltPar(7):
    print("same parents")
else:
    print("Different parents")

ds.UnionBySize(3, 7)

if ds.findUltPar(3) == ds.findUltPar(7):
    print("same parents")
else:
    print("Different parents")






