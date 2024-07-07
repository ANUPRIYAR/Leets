"""
Runtime
544ms Beats 93.95% of users with Python3

848. Shifting Letters
Solved
Medium
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.



Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
shifts.length == s.length
0 <= shifts[i] <= 109
"""
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        cumulative_sum = 0

        prefix_sum = []
        for shift in reversed(shifts):
            cumulative_sum += shift
            prefix_sum.append(cumulative_sum)

        prefix_sum = [num for num in reversed(prefix_sum)]

        answer = []
        for letter, shift in zip(s, prefix_sum):
            new_letter = (ord(letter) - ord('a') + shift) % 26 + ord('a')
            answer.append(chr(new_letter))
        return ''.join(answer)
