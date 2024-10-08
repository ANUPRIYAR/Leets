from typing import List

class Solution:
    def countingSort(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)

        # Counting array
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num - min_val] += 1
        print(f"count : {count}")

        # Cumulative Sum
        for i in range(1, len(count)):
            count[i] += count[i-1]
        print(f"count : {count}")

        # create the output array
        output = [0] * len(nums)
        for num in nums:
            output[count[num- min_val] - 1] = num
            count[num-min_val] -= 1

        return output


input = [-5, 5, 2, 3, 4, 1, - 6]
sol = Solution()
print(sol.countingSort(input))