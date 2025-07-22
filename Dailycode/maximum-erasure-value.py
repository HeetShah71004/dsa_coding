from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        hasX = [False] * (max(nums) + 1)
        ans, wsum = 0, 0
        l, r = 0, 0
        for l, x in enumerate(nums):
            while r < n and not hasX[(y := nums[r])]:
                hasX[y] = True
                wsum += y
                r += 1
            ans = max(ans, wsum)
            hasX[x] = False
            wsum -= x
            if r >= n - 1:
                break
        return ans

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [4, 2, 4, 5, 6]
    print("Input:", nums1)
    print("Output:", sol.maximumUniqueSubarray(nums1))  # Expected: 17
    
    nums2 = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    print("\nInput:", nums2)
    print("Output:", sol.maximumUniqueSubarray(nums2))  # Expected: 8
