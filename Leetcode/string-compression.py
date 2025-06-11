# 443. string-compression

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        idx = 0
        i = 0

        while i < n:
            ch = chars[i]
            count = 0

            # Count the occurrences of the current character
            while i < n and chars[i] == ch:
                count += 1
                i += 1

            # Store the character
            chars[idx] = ch
            idx += 1

            # If count > 1, store its digits
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1

        # Trim the list to the new length
        chars[:] = chars[:idx]
        return idx

s = Solution()
chars = ["a","a","b","b","c","c","c"]
length = s.compress(chars)
print(length)   # Output: 6
print(chars)    # Output: ['a','2','b','2','c','3']

