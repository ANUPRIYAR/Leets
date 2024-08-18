from typing import List
from visualiser.visualiser import Visualiser as vs


# class Solution:
@vs()
def mctFromLeafValues( arr: List[int]) -> int:
    return helper(arr, 0, len(arr) - 1, {})

def helper( arr, l, r, dp):
    if (l, r) in dp:
        return dp[(l, r)]

    if l >= r:
        return 0

    res = float("inf")

    for k in range(l, r):
        rootVal = max(arr[l : k + 1]) * max(arr[k + 1 : r + 1])
        print(f"rootVal: {rootVal}    arr[l:k+1] : {arr[l : k + 1]}, arr[k, r] : {arr[k + 1 : r + 1]}")
        res = min(
            res,
            rootVal + helper(arr, l, k, dp) + helper(arr, k + 1, r, dp),
        )
        print(f"res : {res}")

    dp[(l, r)] = res

    return dp[(l, r)]



def main():
    arr = [7, 6, 4, 3, 2 , 5]
    # sol = Solution()
    print(mctFromLeafValues(arr = [7, 6, 4, 3, 2 , 5]))
    vs.make_animation("mctFromLeaveValues.gif", delay =2)

if __name__ == "__main__":
    main()