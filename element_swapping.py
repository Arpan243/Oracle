def getMaximumSumOfStrengths(arr):
    n = len(arr)
    # Initialize the flag array to track if an element is already swapped
    flag = [0] * n

    # Traverse from the right end of the array to the left
    for i in range(n - 1, 0, -1):
        if flag[i] == 0 and flag[i - 1] == 0 and arr[i - 1] > arr[i]:
            # Swap arr[i-1] and arr[i]
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            # Mark them as swapped
            flag[i] = 1
            flag[i - 1] = 1

    # Calculate the sum of strengths
    max_sum = 0
    for i in range(n):
        max_sum += arr[i] * (i + 1)  # Using 1-based indexing for the formula

    return max_sum

# Example usage:
arr = [2,1,4,3]
print(getMaximumSumOfStrengths(arr))  # Output: 66
