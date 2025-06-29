from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(start: int, end: int) -> int:
            if start >= end:
                return 0
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)

            # Count the number of reverse pairs between two sorted halves
            i = start
            j = mid + 1
            while i <= mid and j <= end:
                if nums[i] > 2 * nums[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1

            # Merge the two sorted halves
            nums[start:end + 1] = sorted(nums[start:end + 1])

            return count

        return merge_sort(0, len(nums) - 1)


# Test Cases
solution = Solution()

# Example 1
nums1 = [1, 3, 2, 3, 1]
print("Example 1 Output:", solution.reversePairs(nums1))  # Output: 2

# Example 2
nums2 = [2, 4, 3, 5, 1]
print("Example 2 Output:", solution.reversePairs(nums2))  # Output: 3
