

def longest_substring(s: str) -> int:
    char_index = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        
        if s[end] in char_index and char_index[s[end]] >= start:
            # Update the start of the substring to the next character after the last occurrence of the current character
            start = char_index[s[end]] + 1
        # Update the index of the current character
        char_index[s[end]] = end
        # Update the maximum length if the current substring is longer
        max_length = max(max_length, end - start + 1)

    return max_length

# Test case
print(longest_substring("abcabcbb"))  # Output: 3
