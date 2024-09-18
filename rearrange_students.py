def minimal_swap_cost(arrA, arrB):
    # Sort both arrays
    arrA.sort()
    arrB.sort()

    # Arrays to keep track of students that need to be swapped
    swap_A = []
    swap_B = []

    # Track frequency of mismatched elements
    freqA = {}
    freqB = {}

    # Fill frequency dictionaries
    for h in arrA:
        freqA[h] = freqA.get(h, 0) + 1
    for h in arrB:
        freqB[h] = freqB.get(h, 0) + 1

    # Check if it's impossible to match heights
    all_heights = set(arrA + arrB)
    for height in all_heights:
        total = freqA.get(height, 0) + freqB.get(height, 0)
        if total % 2 != 0:
            return -1  # If any height appears an odd number of times, it's impossible

    # Find students that need to be swapped
    for height in all_heights:
        excess_in_A = max(0, freqA.get(height, 0) - freqB.get(height, 0)) // 2
        excess_in_B = max(0, freqB.get(height, 0) - freqA.get(height, 0)) // 2

        swap_A.extend([height] * excess_in_A)
        swap_B.extend([height] * excess_in_B)

    # If we have mismatches in swap_A and swap_B, we need to swap the smaller elements
    swap_A.sort()
    swap_B.sort(reverse=True)

    # Calculate the cost of swapping
    min_height = min(arrA + arrB)
    swap_count = len(swap_A)
    total_cost = 0

    for i in range(swap_count):
        total_cost += min(2 * min_height, min(swap_A[i], swap_B[i]))

    return total_cost

# Example usage:
arrA = [4, 2, 2, 2]
arrB = [1, 4, 1, 2]
print(minimal_swap_cost(arrA, arrB))  # Output: 1
