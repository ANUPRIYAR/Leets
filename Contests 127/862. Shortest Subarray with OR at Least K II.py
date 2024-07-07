"""
Same Question : https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/
https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/
3097. Shortest Subarray With OR at Least K II
Medium
You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty
subarray
 of nums, or return -1 if no special subarray exists.

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1

Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10

Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.
Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
=================================================================================================
Pseudo Code  -> we take usual template for Sliding window - Shortest , intialize start to 0 and
window_or to 0
iterate over the numbers using end and take the OR of the numbers
# Since its a bit operation , we do one extra method  ->
we create an array bits = [0]* 32  -> this is to store the bit effect of each number so that we
can reverse it back later
forloop for range-32 and then do AND of num[end] to  1<<i (where in each steps , we are moving 1
from right to left)
then if  we get above 0 , we  increment bits[i] -> bits at postion i
for i in range(32)
     if nums[end] & 1<< i:
            bits[i] += 1

Then we proceed with usual to check the valid condition
if window_or >= k
    we will store minimum of the (end- start +1) in res
    then we start shrinking the array by remOving start
    now to remove start in bit operation
    for loop for 32range
    we will take and of nums[start] and 1 << i , if its > 0 , then we reduce bits at that
    position bits[i] -= 1 and incase bits[i] becomes 0 , we do xor of window_or with 1 << i =>
    window ^= 1<<i
    Then after for loop , we increment start
"""


from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        start = window = 0
        bits = [0] * 32
        for end in range(len(nums)):
            window |= nums[end]
            for i in range(32):
                if nums[end] & (1 << i):
                    bits[i] += 1

            while start <= end and window >= k:
                res = min(res, end - start + 1)    # sliding window template-shortest

                for i in range(32):
                    if nums[start] & (1 << i):
                        bits[i] -= 1
                        if bits[i] == 0:
                            window ^= 1 << i
                start += 1
        return res if res < float('inf') else -1


nums = [1,2,3]
k = 2
sol = Solution()
print(sol.minimumSubarrayLength(nums, k))

# nums = [1,2]
# k = 0
# sol = Solution()
# print(sol.minimumSubarrayLength(nums, k))


# SUMMARY  :