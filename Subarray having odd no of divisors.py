import math
from collections import defaultdict

# Function to check if a number is a perfect square
def is_perfect_square(num):
    if num < 0:
        return False
    root = int(math.sqrt(num))
    return root * root == num

# Function to count subarrays with product having odd number of divisors
def count_subarrays_with_odd_divisors(arr):
    n = len(arr)
    prefix_product_freq = defaultdict(int)
    prefix_product_freq[1] = 1  # Initialize the frequency of product 1 (for the empty subarray)
    
    product = 1
    count = 0
    
    for i in range(n):
        product *= arr[i]
        
        # Check if product divided by the previous product is a perfect square
        for key, freq in list(prefix_product_freq.items()):
            if product % key == 0:
                potential_product = product // key
                if is_perfect_square(potential_product):
                    count += freq
        
        # Update the prefix product frequency
        prefix_product_freq[product] += 1
    
    return count

# Sample usage
arr = [1, 2, 3, 4, 5]  # Sample array
print("Total subarrays with product having odd number of divisors:", count_subarrays_with_odd_divisors(arr))
