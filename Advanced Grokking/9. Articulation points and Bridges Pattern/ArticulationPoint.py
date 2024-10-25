class Solution:
    def __init__(self, vertices):
        self.time = 0
        self.v = vertices
        self.adjlist = [[] for _ in range(self.v)]

    def add_edge(self, u, v):
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)

    def findarticulationpoints(self):
        discoverytime = [-1]* self.v
        low = [-1]* self.v
        parent = [-1]* self.v
        articulation_point = [False]* self.v

        # Perform DFS for each visited node
        for i in range(self.v):
            if discoverytime[i] == -1:
                self.dfs(i, discoverytime, low, parent, articulation_point)

        print("Articulation points in the graph:")
        for i in range(self.v):
            if articulation_point[i] == True:
                print(i , end = " ")

    def dfs(self, curnode, discovery_time, low, parent, articulation_point):
        children = 0
        discovery_time[curnode] = low[curnode] = self.time + 1
        self.time += 1

        for child in self.adjlist[curnode]:
            if discovery_time[child] == -1:
                children += 1
                parent[child] = curnode
                self.dfs(child, discovery_time, low, parent, articulation_point)
                low[curnode] = min(low[child], low[curnode])

                # Case 1: Root node with more than one child
                if parent[curnode] == -1 and children > 1:
                    articulation_point[curnode] = True

                # Case 2: Non-root node where low[child] >= discovery_time[curnode]:
                if parent[curnode] != -1 and low[child] >= discovery_time[curnode]:
                    articulation_point[curnode] = True

            elif child != parent[curnode]:
                low[curnode] = min(low[curnode], discovery_time[child])


graph = Solution(6)  # Example graph with 6 vertices
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)

graph.findarticulationpoints()  # Find and print articulation points
