"""
1854. Maximum Population Year
Solved
Easy
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
Return the earliest year with the maximum population.
Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:

Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.


Constraints:

1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
"""
from typing import List
from collections import defaultdict

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counter = defaultdict(int)
        for birth, death in logs:
            counter[birth] += 1
            counter[death ] -= 1

        population = []
        people = 0
        for time in sorted(counter):
            people += counter[time]
            population.append((time, people))

        max_population = 0
        year = None
        for time, people in population:
            # print(time, people)
            if people > max_population:
                max_population = people
                year = time
        return year if year else logs[0][0]



logs = [[1993,1999],[2000,2010]]
sol = Solution()
print(sol.maximumPopulation(logs))

logs = [[1950,1961],[1960,1971],[1970,1981]]
print(sol.maximumPopulation(logs))