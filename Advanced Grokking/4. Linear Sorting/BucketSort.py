from typing import List

class Solution:
    def bucketSort(self, array: List[int]) -> None:
        if len(array) == 0:
            return

        # Step 1: get the number of buckets
        num_buckets = int(len(array) ** 0.5)
        buckets = [[] for _ in range(num_buckets)]

        # Initialize buckets
        max_val = self.get_max(array)
        for num in array:
            bucket_index = (num * num_buckets)//(max_val + 1)
            buckets[bucket_index].append(num)

        # Step 2 : Sort the bucket
        for bucket in buckets:
            bucket.sort()


        # Step 3: Concatenate the bucket
        index = 0
        for bucket in buckets:
            for num in bucket:
                array[index] = num
                index += 1


    def get_max(self, array):
        max_val = array[0]
        for i in range(len(array)):
            if array[i] > max_val:
                max_val = array[i]

        return max_val


array = [29, 25, 3, 49, 9, 37, 21, 43, 45]
sol = Solution()
sol.bucketSort(array)
print(array)