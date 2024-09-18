def minlen(arr, mxval):
    n = len(arr)
    ans = [-1] * n  
    freq = {}       # To count frequencies of elements in the current window

    left = 0
    distinct_count = 0

    for right in range(n):
        # Add the new element to the dictionary
        if arr[right] not in freq:
            freq[arr[right]] = 0
        if freq[arr[right]] == 0:
            distinct_count += 1
        freq[arr[right]] += 1

        # Shrink the window from the left if there are more than mxval distinct elements
        while distinct_count >= mxval:
            if distinct_count == mxval:
                ans[left] = right - left + 1

            # Remove the element at left from the dictionary
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct_count -= 1
            left += 1

    return ans

arr1 = [1,2,3,2,1]
talcount1 = 3
ans1 = minlen(arr1,talcount1)
print(ans1)

arr1 = [1,1,2,2,3,1,3,2]
talcount1 = 3
ans1 = minlen(arr1,talcount1)
print(ans1)

arr1 = [7,5,3,4,6,1,7,2,4]
talcount1 = 7
ans1 = minlen(arr1,talcount1)
print(ans1)
