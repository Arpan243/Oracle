def count_unique_substrings(s):
    n = len(s)
    char_set = set()  
    left = 0  
    count = 0

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        count += (right - left + 1)
    
    return count

# Example usage:
s = "abdcacef"
print(count_unique_substrings(s)) 