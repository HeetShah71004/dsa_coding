class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False

        vowels_set = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False

        for c in word:
            if not (c.isalpha() or c.isdigit()):
                return False
            if c.isalpha():
                if c in vowels_set:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant


# Test cases
sol = Solution()

# Example 1
word1 = "234Adas"
print(f"Input: {word1} -> Output: {sol.isValid(word1)}")  # Expected: True

# Example 2
word2 = "b3"
print(f"Input: {word2} -> Output: {sol.isValid(word2)}")  # Expected: False

# Example 3
word3 = "a3$e"
print(f"Input: {word3} -> Output: {sol.isValid(word3)}")  # Expected: False
