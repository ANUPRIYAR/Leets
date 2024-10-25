class Solution:
    def __init__(self):
        self.tree = []
        self.arr = []
        self.n = 0

    def buildtree(self, arr, node, start, end, tree):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end)//2
            self.buildtree(arr, node*2, start, mid, tree )
            self.buildtree(arr, node*2 + 1, mid + 1, end, tree)

            tree[node] = tree[node*2] + tree[node*2 + 1]
        return tree[node]

    def query(self, node, start, end, L, R, tree):
        # if the query range is outside the segment range
        if R < start or L > end:
            return 0
        # Complete overlap
        if start >= L and end <= R:
            return tree[node]

        mid = (start + end)//2
        leftsum = self.query(node*2, start , mid, L, R, tree)
        rightsum = self.query(node*2 + 1, mid + 1, end, L, R, tree)

        return leftsum + rightsum

    def update(self, node, start , end, idx, val, tree):
        if start == end:
            tree[node] = val
        else:
            mid = (start + end)//2
            if start <= idx <= mid:
                self.update(node*2, start, mid, idx, val, tree)
            else:
                self.update(2 *node + 1, mid + 1, end, idx, val, tree)

            tree[node] = tree[node*2] + tree[node*2 + 1]



arr = [2, 4, 6, 8]
tree = [0]* 4*(len(arr))

sol = Solution()
sol.buildtree(arr, 1, 0, len(arr)- 1, tree)
print(f"Tree Built : {tree}")
sol.update(1, 0 , len(arr) - 1, 2, 7, tree)
print(f"Updated Tree: {tree}")


# Output
# Tree Built : [0, 20, 6, 14, 2, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0]
# Updated Tree: [0, 21, 6, 15, 2, 4, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0]