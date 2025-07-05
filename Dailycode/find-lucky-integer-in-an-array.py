from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)  # Count frequency
        max_lucky = -1

        for num, count in freq.items():
            if num == count:
                max_lucky = max(max_lucky, num)

        return max_lucky

# Testing with the provided examples
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    arr1 = [2, 2, 3, 4]
    print("Input:", arr1)
    print("Output:", sol.findLucky(arr1))  # Expected Output: 2
    print()

    # Example 2
    arr2 = [1, 2, 2, 3, 3, 3]
    print("Input:", arr2)
    print("Output:", sol.findLucky(arr2))  # Expected Output: 3
    print()

    # Example 3
    arr3 = [2, 2, 2, 3, 3]
    print("Input:", arr3)
    print("Output:", sol.findLucky(arr3))  # Expected Output: -1
