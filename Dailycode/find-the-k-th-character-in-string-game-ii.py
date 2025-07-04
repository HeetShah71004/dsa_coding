from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cnt = 0
        n = len(operations)
        length = pow(2, n - 1)
        for i in range(n - 1, -1, -1):
            if k > length:
                k -= length
                if operations[i] == 1:
                    cnt += 1
            length //= 2
        return chr(ord('a') + (cnt % 26))

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    k1 = 5
    operations1 = [0, 0, 0]
    result1 = sol.kthCharacter(k1, operations1)
    print(f"Input: k = {k1}, operations = {operations1} => Output: '{result1}'")  # Output: "a"

    # Example 2
    k2 = 10
    operations2 = [0, 1, 0, 1]
    result2 = sol.kthCharacter(k2, operations2)
    print(f"Input: k = {k2}, operations = {operations2} => Output: '{result2}'")  # Output: "b"
