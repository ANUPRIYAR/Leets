import math

class Solution:
    def __init__(self, array):
        self.arr = array
        n = len(self.arr)

        # Calculate the size of each block
        self.blocksize = math.ceil(math.sqrt(n))
        self.block = [0]* int(self.blocksize)

        # Precompute the sum of elements for each block
        for i in range(n):
            self.block[i//int(self.blocksize)] += self.arr[i]

        # Function to perform range sum query using square root decomposition
    def query(self, left, right):
        sum_ = 0

        i = left
        while i <= right:
            # Case 1: if i is at the start of the block and entire block lies within[left, right]
            if (i % int(self.blocksize) == 0 )and (i + int(self.blocksize) -1 <= right):
                sum_ += self.block[i//int(self.blocksize)]
                i += int(self.blocksize)
            # Case 2: Else sum the element at index  i directly
            else:
                sum_ += self.arr[i]
                i += 1

        return sum_



input_arr = [1, 3, 5, 7, 9, 11, 13, 15]
sol = Solution(input_arr)

# Query: Sum from index 2 to 6
print(f"Sum from index 2 to 6: {sol.query(2, 6)}")  # Output: 45