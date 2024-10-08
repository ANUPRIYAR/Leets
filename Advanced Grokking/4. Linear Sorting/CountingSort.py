class Solution:
    def countingSort(self, array):
        max_num = self.find_max(array)
        count_array = [0]* (max_num + 1)

        # Frequency
        for i in range(len(array)):
            count_array[array[i]] += 1
        print(f"count_array after updating frequency: {count_array}")

        # Cumulative frequency
        for i in range(1, len(count_array)):
            count_array[i] += count_array[i-1]
        print(f"count_array cumulative frequency: {count_array}")

        # Output Array
        output_array = [0]* len(array)
        for i in range(len(array) - 1, -1 , -1):
            output_array[count_array[array[i]] - 1] = array[i]
            count_array[array[i]] -= 1
        print(f"output_array: {output_array}")
        print(f"count_array: {count_array}")

        for i in range(len(array)):
            array[i] = output_array[i]

        return array

    def find_max(self, array):
        max_ = 0
        for i in range(len(array)):
            if array[i] > max_:
                max_ = array[i]

        return max_



input = [5, 5, 2, 3, 4, 1, 6]
sol = Solution()
print(sol.countingSort(input))