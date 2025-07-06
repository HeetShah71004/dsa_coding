from collections import Counter
from typing import List

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq[self.nums2[index]] -= 1  # Remove old value
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1  # Add new value

    def count(self, tot: int) -> int:
        ans = 0
        for a in self.nums1:
            ans += self.freq[tot - a]  # Check if tot - a exists in nums2
        return ans

# Example usage
commands = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
arguments = [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]

output = []
obj = None

for cmd, arg in zip(commands, arguments):
    if cmd == "FindSumPairs":
        obj = FindSumPairs(*arg)
        output.append(None)
    elif cmd == "add":
        obj.add(*arg)
        output.append(None)
    elif cmd == "count":
        res = obj.count(*arg)
        output.append(res)

print(output)
