from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(arr, k):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    sumsleft = check_subset_sum(left)
    sumsright = check_subset_sum(right)
    print(f"sumsleft : {sumsleft}")
    print(f"sumsright:  {sumsright}")
    sumsright.sort()
    count = 0
    for sleft in sumsleft:
        if sleft == k:
            count += 1
        if sleft > k:
            continue
        remaining = k - sleft
        print(f"sleft :{sleft} , remaining : {remaining}")
        idx = binary_search(sumsright, remaining)
        if idx != -1:
            start, end = idx, idx
            while arr[start] == remaining:
                start -= 1
            while arr[end] == remaining:
                end += 1
            count += (end - start + 1)
    return count

def check_subset_sum(arr):
    total_subsets = 1 << len(arr)
    sums = []
    for mask in range(total_subsets):
        sum_ = 0
        for i in range(len(arr)):
            if mask & (1 << i) != 0:
                sum_ += arr[i]
        sums.append(sum_)
    return sums

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1




nums2 = [1, 2, 3, 4, 5]
x2 = 5
print("Number of subsets that sum to", x2, ":", subsetSumToK(nums2, x2))
# Expected output: 3











#
# arr = [2, 4, 6, 10]
# k = 16
# print(subsetSumToK(4, k, arr ))