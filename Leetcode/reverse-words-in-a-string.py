#  151. reverse-words-in-a-string

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = s[::-1]  # Reverse the entire string
        ans = ""
        i = 0

        while i < n:
            word = ""
            # Skip any leading spaces
            while i < n and s[i] == ' ':
                i += 1

            # Build the word
            while i < n and s[i] != ' ':
                word += s[i]
                i += 1

            # Reverse the word and add to result
            if word:
                ans += " " + word[::-1]

        return ans.strip()  # Remove leading space


# Test cases
sol = Solution()
test_cases = [
    "the sky is blue",
    "  hello world  ",
    "a good   example",
]

for i, test in enumerate(test_cases, 1):
    output = sol.reverseWords(test)
    print(f"Example {i}:")
    print(f"Input: \"{test}\"")
    print(f"Output: \"{output}\"\n")

