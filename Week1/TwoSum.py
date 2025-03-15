# sol:(Brute Force)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
    
nums = [2, 7, 11, 15]
target = 9

sol1 = Solution()
print(sol1.twoSum(nums, target)) 

