# 33. search in rotated sorted array

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Constraints:
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4

class Solution:
    def search(self, A: list[int], tar: int) -> int:
        st, end = 0, len(A) - 1

        while st <= end:
            mid = st + (end - st) // 2

            if A[mid] == tar:
                return mid

            # Check if left part is sorted
            if A[st] <= A[mid]:
                if A[st] <= tar <= A[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:  # Right part is sorted
                if A[mid] <= tar <= A[end]:
                    st = mid + 1
                else:
                    end = mid - 1

        return -1
    
# Instantiate the class
sol = Solution()

# Test cases
print("Example 1:")
print("Input: nums = [4,5,6,7,0,1,2], target = 0")
print("Output:", sol.search([4,5,6,7,0,1,2], 0))  # Output: 4

print("\nExample 2:")
print("Input: nums = [4,5,6,7,0,1,2], target = 3")
print("Output:", sol.search([4,5,6,7,0,1,2], 3))  # Output: -1

print("\nExample 3:")
print("Input: nums = [1], target = 0")
print("Output:", sol.search([1], 0))  # Output: -1

