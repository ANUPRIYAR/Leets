import math

seg = [0] * 50
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def build(ind, low, high):
    if low == high:
        seg[ind] = a[low]
        return

    mid = (low + high)//2
    build(2*ind +1, low, mid)
    build(2*ind+2, mid +1, high)
    seg[ind] = max(seg[2*ind +1], seg[2*ind + 2])


def query(ind, low, high, l, r):
    if low >= l and high <= r:
        return seg[ind]
    if high < l or low > r:
        return -math.inf

    mid = (low + high)//2
    left = query(2*ind + 1, low, mid, l, r)
    right = query(2*ind + 2, mid +1, high, l, r)
    return max(left, right)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
build(0, 0, 9)
print(f"segment Tree: {seg}")

print(f"query max in range 3-5 : {query(0, 0, 9, 3, 5)}")

# segment Tree: [10, 5, 10, 3, 5, 8, 10, 2, 3, 4, 5, 7, 8, 9, 10, 1, 2, 0, 0, 0, 0, 0, 0, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# query max in range 3-5 : 6
