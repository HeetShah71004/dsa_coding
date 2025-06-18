from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.seen = set()  # to avoid duplicate combinations

    def getAllCombinations(self, arr: List[int], idx: int, target: int,
                           ans: List[List[int]], combin: List[int]):
        if idx == len(arr) or target < 0:
            return

        if target == 0:
            key = tuple(combin)
            if key not in self.seen:
                ans.append(list(combin))
                self.seen.add(key)
            return

        # include current element once
        combin.append(arr[idx])
        self.getAllCombinations(arr, idx + 1, target - arr[idx], ans, combin)

        # include current element multiple times
        self.getAllCombinations(arr, idx, target - arr[idx], ans, combin)

        # backtrack
        combin.pop()

        # exclude current element
        self.getAllCombinations(arr, idx + 1, target, ans, combin)

    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        ans = []
        combin = []
        self.getAllCombinations(arr, 0, target, ans, combin)
        return ans
sol = Solution()
arr = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(arr, target))
# Possible Output: [[7], [2, 2, 3]]
