from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n, prev, cnt = len(nums), nums[0], 0
        diff = [0, 0]
        i = 0
        while i < n:
            while i < n and prev == nums[i]:
                i += 1
            if i == n:
                break
            bigger = 1 if nums[i] > prev else 0
            diff[bigger] = 1
            cnt += diff[bigger] and diff[1 - bigger]
            diff[1 - bigger] = 0
            prev = nums[i]
            i += 1
        return cnt

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [2, 4, 1, 1, 6, 5]
    print("Input:", nums1)
    print("Output:", sol.countHillValley(nums1))  # Expected Output: 3

    # Example 2
    nums2 = [6, 6, 5, 5, 4, 1]
    print("Input:", nums2)
    print("Output:", sol.countHillValley(nums2))  # Expected Output: 0
