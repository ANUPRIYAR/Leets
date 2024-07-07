"""
Runtime
97 ms Beats 55.35% of users with Python3
Memory
Beats 86.75% of users with Python3

https://leetcode.com/problems/longest-subsequence-with-limited-sum/

2389. Longest Subsequence With Limited Sum
Easy
You are given an integer array nums of length n, and an integer array queries of length m.
Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
Example 2:

Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.


Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 106
"""
# Patters: It combines Prefix sum , Binary search, Greedy algorithm
from typing import List
class Solution:
    def binary_search(self, array, key):
        start = 0
        end = len(array) - 1
        while start <= end:
            mid = (start + end)//2
            if key == array[mid]:
                return mid
            elif key < array[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if array[mid] > key:
            return mid - 1
        return mid

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # sort the arrays
        nums.sort()

        prefix_sum = []
        rs = 0
        for num in nums:
            rs += num
            prefix_sum.append(rs)

        result = []
        for query in queries:
            index = self.binary_search(prefix_sum, query)
            result.append(index + 1)

        return result


nums = [4,5,2,1]
queries = [3,10,21]
sol = Solution()
print(sol.answerQueries(nums, queries))

nums = [2,3,4,5]
queries = [1]
print(sol.answerQueries(nums, queries))



