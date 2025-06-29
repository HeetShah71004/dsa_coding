class Solution:
    def binarySearchRightmost(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def numSubseq(self, nums, target):
        n = len(nums)
        mod = 10**9 + 7
        nums.sort()

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % mod

        answer = 0
        for left in range(n):
            remaining = target - nums[left]
            right = self.binarySearchRightmost(nums, remaining) - 1
            if left <= right:
                answer = (answer + power[right - left]) % mod

        return answer


# Test Cases
solution = Solution()

# Example 1
nums1 = [3, 5, 6, 7]
target1 = 9
print("Example 1 Output:", solution.numSubseq(nums1, target1))  # Output: 4

# Example 2
nums2 = [3, 3, 6, 8]
target2 = 10
print("Example 2 Output:", solution.numSubseq(nums2, target2))  # Output: 6

# Example 3
nums3 = [2, 3, 3, 4, 6, 7]
target3 = 12
print("Example 3 Output:", solution.numSubseq(nums3, target3))  # Output: 61
