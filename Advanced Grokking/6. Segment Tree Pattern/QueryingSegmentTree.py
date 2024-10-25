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

# Example usage
arr = [2, 4, 6, 8, 10, 12]
n = len(arr)
tree = [0] * (4 * n)
sol = Solution()
sol.arr = arr
sol.n = n
sol.tree = tree

sol.buildtree(arr, 1, 0, n - 1, tree)
print(tree)
result = sol.query(1, 0, n - 1, 1, 4, tree)
print(result)

