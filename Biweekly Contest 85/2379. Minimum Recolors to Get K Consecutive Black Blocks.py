"""
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
2379. Minimum Recolors to Get K Consecutive Black Blocks [Easy]
Solved
Pattern: Sliding Window

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
representing the color of the ith block. The characters 'W' and 'B' denote the colors white and
black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k
consecutive black blocks.


Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3
operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.


Constraints:
n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
"""


# Pattern: Sliding window


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Edge Case
        if len(blocks) == 1:
            if blocks[0] == 'W':
                return 1
            else:
                return 0

        start = 0
        min_count = 999999
        count = 0
        for end in range(len(blocks)):
            # Get the count of W (operations)
            if blocks[end] == 'W':
                count += 1

            # (atleast 1 k consecutive black blocks)
            while (end - start + 1) >= k and start <= end:
                min_count = min(min_count, count)  # we have to find min operations to get k consecutive black blocks
                left_char = blocks[start]
                if left_char == 'W':
                    count -= 1

                start += 1

        return min_count if min_count != 999999 else 0
