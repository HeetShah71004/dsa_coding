#  125. valid-palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: s = "race a car"
# Output: false

# Example 3:
# Input: s = " "
# Output: true

class Solution:
    def isAlphaNum(self, ch):
        return ch.isalnum()  # checks if alphanumeric (letters or digits)

    def isPalindrome(self, s: str) -> bool:
        st, end = 0, len(s) - 1

        while st < end:
            while st < end and not self.isAlphaNum(s[st]):
                st += 1
            while st < end and not self.isAlphaNum(s[end]):
                end -= 1
            if s[st].lower() != s[end].lower():
                return False
            st += 1
            end -= 1
        return True
    
sol = Solution()

# Test Cases
inputs = [
    "A man, a plan, a canal: Panama",  # True
    "race a car",                      # False
    " ",                               # True (empty or only space is a palindrome)
    "0P",                              # False
    "Madam",                           # True
]

for s in inputs:
    print(f"Input: '{s}' --> Output: {sol.isPalindrome(s)}")
