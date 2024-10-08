import math

class Query:
    def __init__(self, left, right, index):
        self.left = left
        self.right = right
        self.index = index

class Solution:
    # Function to process all queries using Mo Algorithm
    def processQueries(self, arr, queries):
        n = len(arr)
        q = len(queries)
        blocksize = math.ceil(math.sqrt(n))
        result = [0]* q

        # Sort the queries
        queries.sort(key = lambda q: (q.left//blocksize, q.right))

        # Initialize Current left and currentright and currentsum
        currentleft , currentright = 0, 0
        currentsum = arr[0]

        for query in queries:
            left = query.left
            right = query.right

            while currentright < right:
                currentright += 1
                currentsum += arr[currentright]

            while currentright > right:
                currentsum -= arr[currentright]
                currentright -= 1


            while currentleft < left:
                currentsum -= arr[currentleft]
                currentleft += 1


            while currentleft > left:
                currentleft -= 1
                currentsum += arr[currentleft]

            result[query.index] = currentsum

        return result


input = [1, 3, 5, 7, 9, 11, 13, 15]

# Array of queries, each query asks for the sum of a subarray
queries = [
    Query(2, 6, 0),  # Sum from index 2 to 6
    Query(0, 4, 1),  # Sum from index 0 to 4
    Query(3, 5, 2)  # Sum from index 3 to 5
]

sol = Solution()
results = sol.processQueries(input, queries)

# Print the results of each query
for i in range(len(results)):
    print(f"Sum of Query {i} : {results[i]}")

# Output
# Sum of Query 0 : 45
# Sum of Query 1 : 25
# Sum of Query 2 : 27