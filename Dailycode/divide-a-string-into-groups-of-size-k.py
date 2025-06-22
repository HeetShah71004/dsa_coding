class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        n = len(s)
        groups = (n + k - 1) // k
        result = []

        for i in range(groups):
            group = ''
            for j in range(k):
                index = i * k + j
                if index < n:
                    group += s[index]
                else:
                    group += fill  # Padding
            result.append(group)

        return result

# Create an instance of the class
sol = Solution()

# Example 1
s1 = "abcdefghi"
k1 = 3
fill1 = "x"
print("Example 1 Output:", sol.divideString(s1, k1, fill1))  # Output: ["abc","def","ghi"]

# Example 2
s2 = "abcdefghij"
k2 = 3
fill2 = "x"
print("Example 2 Output:", sol.divideString(s2, k2, fill2))  # Output: ["abc","def","ghi","jxx"]
