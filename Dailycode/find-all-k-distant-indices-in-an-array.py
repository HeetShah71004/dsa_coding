from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = [] 
        right = 0

        for i in range(n):
            if nums[i] == key:
                left = max(right, i - k)
                right = min(n, i + k + 1)
                ans.extend(range(left, right))

        return sorted(set(ans))  # Remove duplicates and sort the result


# Example usage:
if __name__ == "__main__":
    # Input: Provide a space-separated list of numbers
    nums = list(map(int, input("Enter nums (space-separated): ").split()))
    key = int(input("Enter key: "))
    k = int(input("Enter k: "))

    sol = Solution()
    result = sol.findKDistantIndices(nums, key, k)
    print("Output:", result)
