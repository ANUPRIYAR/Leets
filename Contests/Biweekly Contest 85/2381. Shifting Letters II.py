"""
https://leetcode.com/problems/shifting-letters-ii/description/
2381. Shifting Letters II  [Medium]
Pattern : Array, String , Prefix sum

You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
Return the final string after all such shifts to s are applied.

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".


Constraints:

1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict

# THIS DID NOT WORK WITH BELOW INPUT : See right solution at the end
# s ="xuwdbdqik"
# shifts =[[4,8,0],[4,4,0],[2,4,0],[2,4,0],[6,7,1],[2,2,1],[0,2,1],[8,8,0],[1,3,1]]
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_counter = defaultdict(int)
        for start, end, direction in shifts:
            if direction == 0:
                shift_counter[start] -= 1
                shift_counter[end + 1] += 1
            else:
                shift_counter[start] += 1
                shift_counter[end + 1] -= 1

        total_shifts = 0
        ordering  = []
        for shift in sorted(shift_counter):
            total_shifts += shift_counter[shift]
            ordering.append((shift, total_shifts))

        print(ordering)

        new_string = []
        for letter, shift in zip(s,ordering):
            new_letter = chr((ord(letter) - 97 + shift[1])% 26 + 97)
            print(new_letter)
            new_string.append(new_letter)
        if len(s) != len(new_string):
            new_string.append(s[len(new_string) -1 + (len(s)  -len(new_string))])
        return ''.join(new_string)

# s = "abc"
# shifts = [[0,1,0],[1,2,1],[0,2,1]]
# sol = Solution()
# print(f"answer: {sol.shiftingLetters(s, shifts)}")
#
# s = "dztz"
# shifts = [[0,0,0],[1,1,1]]
# print(f"answer: {sol.shiftingLetters(s, shifts)}")
#
# s ="xuwdbdqik"
# shifts =[[4,8,0],[4,4,0],[2,4,0],[2,4,0],[6,7,1],[2,2,1],[0,2,1],[8,8,0],[1,3,1]]
# print(f"answer: {sol.shiftingLetters(s, shifts)}")
#============================================================
# gave wrong  answer: ywxcxcqgk , that's because in the ordering , its missing shift of one index ,
# hence this a wrong logic to do this . Instead, we should take cumulative sum
# ordering : [(0, 1), (1, 2), (2, 1), (3, -1), (4, -4), (5, -1), (6, 0), (8, -2), (9, 0)]
#============================================================

# Runtime
#1009 ms Beats 72.55% of users with Python3
# Working Solution
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Taking array instead of defaultdict
        shift_counter = [0 for _ in range(len(s) + 1)]
        for start, end, direction in shifts:
            if direction == 0:
                shift_counter[start] -= 1
                shift_counter[end + 1] += 1
            else:
                shift_counter[start] += 1
                shift_counter[end + 1] -= 1

        # Taking cumulative shift
        answer = []
        # iterating over string
        for i in range(len(s)):
            if i != 0:  # because at 0 , we cant add it with its previous number
                shift_counter[i] += shift_counter[i-1]
            new_char = chr((ord(s[i]) - ord('a') + shift_counter[i]) % 26 + ord('a'))
            answer.append(new_char)
        return ''.join(answer)


s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
sol = Solution()
print(f"answer: {sol.shiftingLetters(s, shifts)}")

s = "dztz"
shifts = [[0,0,0],[1,1,1]]
print(f"answer: {sol.shiftingLetters(s, shifts)}")

s ="xuwdbdqik"
shifts =[[4,8,0],[4,4,0],[2,4,0],[2,4,0],[6,7,1],[2,2,1],[0,2,1],[8,8,0],[1,3,1]]
print(f"answer: {sol.shiftingLetters(s, shifts)}")