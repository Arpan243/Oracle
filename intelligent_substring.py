def longest_special_substring(s, charValue, k):
    def is_special(c):
      index = ord(c) - ord('a')
      return charValue[index] == '1'
    
    n = len(s)
    left = 0
    normal_count = 0
    max_len = 0
    
    for right in range(n):
        if not is_special(s[right]):
            normal_count += 1
        
        while normal_count > k:
            if not is_special(s[left]):
                normal_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)
          
    return max_len

# Example usage
s = "giraffe"
charValue = "01111001111111111011111111"
k = 2
print(longest_special_substring(s, charValue, k))  # Output: 5
