# Given a set of n integers where n <= 40, and each integer is at most 1012, determine the maximum sum subset with a sum less than or equal to S, where S <= 1012.

# nums = {3, 15, 14, 9, 6, 2}
# S = 10

from typing import List

class Solution:
    def maxSubsetSum(self, nums: List[int], S: int) -> int:
        n = len(nums)
        mid = n//2
        left = nums[:mid]
        right = nums[mid:]

        sumleft = self.generateSubsetSums(left)
        sumright = self.generateSubsetSums(right)

        sumright.sort()
        maxsum = 0

        for sleft in sumleft:
            if sleft > S:
                continue
            remaining = S - sleft
            # Binary search to find the largest sum in sumRight <= remaining
            idx = self.upperBound(sumright, remaining)

            if idx >= 0:
                sright = sumright[idx]
                total = sleft + sright
                if total > maxsum:
                    maxsum = total

        return maxsum


    def generateSubsetSums(self, arr):
        n = len(arr)
        totalSubsets = 1 << n
        subset_sums = []

        for mask in range(totalSubsets):
            sum_ = 0
            for i in range(len(arr)):
                if (mask & (1 << i)) != 0:
                    sum_ += arr[i]
            subset_sums.append(sum_)

        return subset_sums


    def upperBound(self, arr, target):
        low = 0
        high = len(arr) - 1
        result = -1

        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] <= target:
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result




