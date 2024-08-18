"""
https://leetcode.com/problems/points-that-intersect-with-cars/description/
2848. Points That Intersect With Cars
Easy
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

Return the number of integer points on the line that are covered with any part of a car.

Example 1:

Input: nums = [[3,6],[1,5],[4,7]]
Output: 7
Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
Example 2:

Input: nums = [[1,3],[5,8]]
Output: 7
Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

Constraints:
1 <= nums.length <= 100
nums[i].length == 2
1 <= starti <= endi <= 100
"""
# Pattern : Linesweep + Hashtable + sorting
from typing import List
import collections

# class Solution:
#     def numberOfPoints(self, nums: List[List[int]]) -> int:
#         counter = collections.Counter()
#
#         for start, end in nums:
#             counter[start] += 1
#             counter[end +1] -= 1
#         print(counter)
#
#         s = res= 0
#         for key, value in sorted(counter.items()):
#             if s == 0:
#                 start = key
#             s += value
#
#             if s == 0:
#                 res += key - start
#         return res

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        events = []
        for start, end in nums:
            events.append([start, 1])
            events.append([end, -1])
        events.sort()

        count = 0
        active_cars = 0
        for pos, event_type in events:
            if event_type == 1:
                active_cars += 1
            else:
                active_cars -= 1
            count += 1 if active_cars > 0 else 0

            # if active_cars > 0 :
            #     count += 1   # Cars are intersecting at this point
        return count


nums = [[3,6],[1,5],[4,7]]
sol = Solution()
print(sol.numberOfPoints(nums))



nums = [[1,3],[5,8]]
sol = Solution()
print(sol.numberOfPoints(nums))