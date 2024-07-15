"""
2251. Number of Flowers in Full Bloom
Hard
Topics
Companies
Hint
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.



Example 1:


Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:


Input: flowers = [[1,10],[3,3]], people = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.


Constraints:

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= people.length <= 5 * 104
1 <= people[i] <= 109
"""
from typing import List
from collections import defaultdict
import math
from bisect import bisect_left
####################### Memory Limit exceeded  #################################
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        counter = defaultdict(int)
        min_start = 999999
        max_end = -math.inf
        flowers.sort(key=lambda x: x[0])
        for start, end in flowers:
            min_start = min(min_start, start)
            max_end = max(max_end, end)
            counter[start] += 1
            counter[end + 1] -= 1

        array = [0]* (max_end - min_start + 2)
        cur_value = 0
        for i in range(len(array)):
            if (i + min_start) in counter:
                cur_value  = cur_value + counter[i + min_start]
                array[i] =  cur_value
            else:
                array[i] = cur_value

        answer = []
        for arrival_time in people:
            if arrival_time < min_start:
                answer.append(0)
            elif arrival_time > max_end:
                answer.append(0)
            else:
                answer.append(array[arrival_time - min_start])

        return answer



# Another solution
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        counter = defaultdict(int)
        flowers.sort(key=lambda x: x[0])
        # create dict to increment dict of start and decrement dict of end + 1
        for start, end in flowers:
            counter[start] += 1
            counter[end + 1] -= 1

        bloomed_flowers = 0
        timer = []
        # create a 2D array with keys of counter and number of active events, where time = key
        for time in sorted(counter):
            bloomed_flowers += counter[time]
            timer.append((time,bloomed_flowers))

        print(f"timer: {timer}")

        answer = []
        # Iterate through arrival time of people and locate the index of arrival_time in the 2D array.
        # if arrival time is not in the range of counter,Bisect_left will return index as last_index  + 1
        # or if arrival time is not in counter , bisect_left will return index where the element should ideally be placed.
        # It will return correct index , if element is found in array
        # In linesweep usually the last count(which is max_end of events) will be 0 , since all the events have ended.
        # Hence, if the element you are finding is not actually in counter
        # then you just reduce idx by 1(so if idx is 0 , then it will return last element, which is 0
        # and if idx >= length, then also it will return last element which is 0)

        for arrival_time in people:
            idx = bisect_left(timer, arrival_time, key=lambda x:x[0])
            print(idx)
            if arrival_time not in counter:
                idx -= 1
                print(f"idx now: {idx}")
            answer.append(timer[idx][1])
        return answer











flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]
sol = Solution()
print(f"answer : {sol.fullBloomFlowers(flowers, people)}")

flowers = [[19,37],[19,38],[19,35]]
people = [6,7,21,1,13,37,5,37,46,43]
sol = Solution()
print(f"answer : {sol.fullBloomFlowers(flowers, people)}")

flowers = [[50,50],[36,49],[6,16],[21,38],[43,44],[48,50],[28,40],[30,33]]
people = [6,44,13,48,6,11,1,35]
sol = Solution()
print(f"answer : {sol.fullBloomFlowers(flowers, people)}")