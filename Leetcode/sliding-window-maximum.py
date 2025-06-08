# 239. sliding-window-maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        # First window
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)

        # Process the rest of the elements
        for i in range(k, len(nums)):
            res.append(nums[dq[0]])

            # Remove indices not in the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller values
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

        # Add the maximum for the last window
        res.append(nums[dq[0]])

        return res

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# Output: [3,3,5,5,6,7]
