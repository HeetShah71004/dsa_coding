class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg_count = self.binary_search(nums, 0) 
        pos_count = len(nums) - self.binary_search(nums, 1)
        return max(neg_count, pos_count)

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        result = len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        
        return result
        
# Time complexity: O(logn)
# Space complexity: O(1)

nums = [-2,-1,-1,1,2,3,4]
solution = Solution()

print(solution.maximumCount(nums))  