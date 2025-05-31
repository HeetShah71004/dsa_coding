# 287. find-the-duplicate-number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3

class Solution:
    def findDuplicate(self, arr: list[int]) -> int:
        # Phase 1: Finding the intersection point
        slow = arr[0]
        fast = arr[0]

        while True:
            slow = arr[slow]       # +1 step
            fast = arr[arr[fast]] # +2 steps
            if slow == fast:
                break

        # Phase 2: Finding the entrance to the cycle (duplicate number)
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]  # +1 step
            fast = arr[fast]  # +1 step

        return slow
    
sol = Solution()
arr = [1, 3, 4, 2, 2]
print(sol.findDuplicate(arr))  # Output: 2
arr = [3,1,3,4,2] 
print(sol.findDuplicate(arr)) # Output: 3
arr = [3,3,3,3,3]
print(sol.findDuplicate(arr)) # Output: 3
