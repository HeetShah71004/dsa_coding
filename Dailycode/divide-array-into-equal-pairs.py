class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for count in counter.values():
            if count % 2 != 0:
                return False
        
        return True

# Test case

# nums = [1, 2, 3, 4]
nums = [3,2,3,2,2,2]
print(Solution().divideArray(nums)) 