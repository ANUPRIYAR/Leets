def buildTree(arr, node, start, end, tree):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end)//2
        buildTree(arr, node*2, start, mid, tree)
        buildTree(arr, node*2 + 1, mid + 1, end, tree)

        # combine left and right node values
        tree[node] = tree[node*2] + tree[node* 2+ 1]

    return tree[node]


arr = [2,4,6,8,10, 12]
tree = [0] * (4* len(arr))
buildTree(arr, 1, 0, len(arr)- 1, tree)
print(tree)


# Output
# [0, 42, 12, 30, 6, 6, 18, 12, 2, 4, 0, 0, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


"""
Complexity Analysis
==================
Time Complexity:
Build Operation: The build operation takes O(N) time because it processes each element of the array 
exactly once.

Space Complexity:
The space complexity of the Segment Tree is O(N) because we need to store the tree in an array of 
size 4*n . This extra space ensures that all nodes, including internal and leaf nodes, 
have enough space to be stored efficiently.
"""