from collections import defaultdict

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        modulo_map = defaultdict(lambda: defaultdict(int))
        res = 0

        for i, num in enumerate(nums):
            mod_i = i % k

            if num in modulo_map:
                for mod_j, count in modulo_map[num].items():
                    if (mod_i * mod_j) % k == 0:
                        res += count
            modulo_map[num][mod_i] += 1

        return res

# Test cases

nums = [3,1,2,2,2,1,3]
k = 2
solution = Solution()
result = solution.countPairs(nums, k)
print(result)  # Output: 4