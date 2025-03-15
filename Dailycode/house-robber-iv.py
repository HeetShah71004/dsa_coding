class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def can_steal_k_houses(capability):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2 
                else:
                    i += 1
            return count >= k
        
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if can_steal_k_houses(mid):
                right = mid
            else:
                left = mid + 1
                
        return left    


nums = [2,3,5,9]
k = 2
print(Solution().minCapability(nums, k)) 