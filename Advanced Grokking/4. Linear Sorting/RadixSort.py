def get_max(array):
    max_val = array[0]
    for i in range(len(array)):
        if array[i] > max_val:
            max_val = array[i]
    return max_val

def counting_sort(array, exp):
    output = [0]* len(array)
    count = [0]* 10

    # get frequency if each element
    for i in range(len(array)):
        digit = (array[i]//exp) % 10
        count[digit] += 1

    # cumulative frequency
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Build output array and traverse array in reverse
    for i in range(len(array) - 1, -1, -1):
        digit = (array[i]//exp) % 10
        output[count[digit] - 1] = array[i]
        count[digit] -= 1

    # copy array from output
    for i in range(len(array)):
        array[i] = output[i]

def radix_sort(array):
    max_val = get_max(array)
    exp = 1
    while max_val//exp > 0:
        counting_sort(array, exp)
        exp *= 10



array2 = [123, 456, 789, 234, 567, 890, 345, 678]
radix_sort(array2)
print("Sorted array 2:", array2)

# Output : Sorted array 2: [123, 234, 345, 456, 567, 678, 789, 890]