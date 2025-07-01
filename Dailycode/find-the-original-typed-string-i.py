class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Step 1: Start with 1 possible original (no mistake)
        ans = 1

        # Step 2: Loop from the second character
        for i in range(1, len(word)):
            # Step 3: If current and previous characters are the same
            if word[i] == word[i - 1]:
                ans += 1  # Step 4: Count as a possible duplication

        # Step 5: Return total count
        return ans

# Create an instance of Solution
sol = Solution()

# Example 1
word1 = "abbcccc"
print("Input:", word1)
print("Output:", sol.possibleStringCount(word1))  # Expected: 5
print()

# Example 2
word2 = "abcd"
print("Input:", word2)
print("Output:", sol.possibleStringCount(word2))  # Expected: 1
print()

# Example 3
word3 = "aaaa"
print("Input:", word3)
print("Output:", sol.possibleStringCount(word3))  # Expected: 4
