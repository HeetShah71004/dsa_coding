class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def solve(text: str, pattern: str, score: int):
            stack = []
            points = 0
            for char in text:
                if stack and stack[-1] == pattern[0] and char == pattern[1]:
                    stack.pop()
                    points += score
                else:
                    stack.append(char)
            return points, "".join(stack)

        if x >= y:
            points1, remaining_s = solve(s, "ab", x)
            points2, _ = solve(remaining_s, "ba", y)
        else:
            points1, remaining_s = solve(s, "ba", y)
            points2, _ = solve(remaining_s, "ab", x)

        return points1 + points2

# Testing with examples
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    s1 = "cdbcbbaaabab"
    x1, y1 = 4, 5
    print("Example 1:")
    print(f"Input: s = \"{s1}\", x = {x1}, y = {y1}")
    print(f"Output: {sol.maximumGain(s1, x1, y1)}")  # Expected: 19

    # Example 2
    s2 = "aabbaaxybbaabb"
    x2, y2 = 5, 4
    print("\nExample 2:")
    print(f"Input: s = \"{s2}\", x = {x2}, y = {y2}")
    print(f"Output: {sol.maximumGain(s2, x2, y2)}")  # Expected: 20
