from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total_distinct = len(set(nums))
        count = defaultdict(int)
        left = res = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) == total_distinct:
                res += len(nums) - right
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return res

# Test cases
nums = [1,3,1,2,2]
solution = Solution()
print(solution.countCompleteSubarrays(nums))  # Output: 4