# Example Problem: Serialize and Deserialize an Array of Integers
# Problem Statement
# Given an array of integers, write a function to serialize the array into a string and
# another function to deserialize the string back into the original array.
# The serialization should be done using a comma-separated format.
#
# Example
# Input: [1, 2, 3, 4, 5]
# Serialized Output: "1,2,3,4,5"
# Deserialized Output: [1, 2, 3, 4, 5]


class Solution:
    def serialize(self, array):
        serialized_string = ""

        for i in range(len(array)):
            serialized_string += str(array[i])

            # add a comma after each element except the last one
            if i < len(array) - 1:
                serialized_string += ","

        return serialized_string

    def deserialize(self, serialized_string):
        array_list = []
        currentnum = ""
        for i in range(len(serialized_string)):
            currentchar = serialized_string[i]

            if currentchar == ",":
                array_list.append(int(currentnum))
                currentnum = ""
            else:
                currentnum += currentchar

        array_list.append(int(currentnum))

        return array_list




# Example usage
inputArray = [1, 2, 3, 4, 5]

sol = Solution()

# Serialize the input array
serializedOutput = sol.serialize(inputArray)
print("Serialized Output:", serializedOutput)  # Output: "1,2,3,4,5"

# Deserialize the string back to an array
deserializedOutput = sol.deserialize(serializedOutput)
print("Deserialized Output:", " ".join(map(str, deserializedOutput)))  # Output: "1 2 3 4 5"