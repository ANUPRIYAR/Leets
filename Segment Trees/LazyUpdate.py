
def update_range(seg, lazy, node, start, end, l, r, value):
    if lazy[node] != 0:
        seg[node] += (end - start + 1 ) *lazy[node]

        if start != end:
            lazy[ 2 *node +1] += lazy[node]
            lazy[2 * node + 2] += lazy[node]
        lazy[node] = 0  # reset the pending update for the current node

    if start > end or start > r or end < l:  # does not overlap
        return

    if start >= l and end <= r:
        seg[node] += (end - start + 1)*value
        if start != end:
            lazy[node*2 +1] += value
            lazy[node*2 + 2] += value

        return

    #  if range partially overlaps
    mid = (start + end)//2
    # Recursively update left and right child
    update_range(seg, lazy, node, start , mid, l, r, value)
    update_range(seg, lazy, node, mid + 1, end, l, r, value)
    # Update current node based on its children
    seg[node] = seg[2*node + 1] + seg[2*node + 2]


def query_range(seg, lazy, node, start, end, l, r):
    if(start > end) or (start > r) or (end < l):
        return 0
    if lazy[node] != 0:
        seg[node] += (end - start + 1)*lazy[node]

        if start != end:
            lazy[node*2 +1] += lazy[node]
            lazy[node*2 + 2] += lazy[node]
        lazy[node] = 0

    if start >= l and end <= r:
        return seg[node]

    mid = (start + end)/2
    p1  = query_range(seg, lazy, node*2 + 1, start, mid, l, r)
    p2 = query_range(seg, lazy, node*2 + 2, mid +1, end, l, r)
    return p1 + p2

