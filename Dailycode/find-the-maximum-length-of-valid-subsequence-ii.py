from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r = [num % k for num in nums]
        l = [[] for _ in range(k)]
        for i, x in enumerate(r):
            l[x].append(i)
        
        m = max(len(lst) for lst in l) if k > 0 else 0
        
        if k == 0 or k == 1:
            return m
        
        for x in range(k):
            for y in range(x + 1, k):
                a = l[x]
                b = l[y]
                la = len(a)
                lb = len(b)
                if la == 0 and lb == 0:
                    continue
                i = j = 0
                sx = sy = 0
                while i < la or j < lb:
                    if j == lb or (i < la and a[i] < b[j]):
                        nx = 1
                        if sy > 0:
                            nx = sy + 1
                        if nx > sx:
                            sx = nx
                        i += 1
                    else:
                        ny = 1
                        if sx > 0:
                            ny = sx + 1
                        if ny > sy:
                            sy = ny
                        j += 1
                c = max(sx, sy)
                if c > m:
                    m = c
        return m

# Example 1
nums1 = [1, 2, 3, 4, 5]
k1 = 2
print("Example 1 Output:", Solution().maximumLength(nums1, k1))  # Expected: 5

# Example 2
nums2 = [1, 4, 2, 3, 1, 4]
k2 = 3
print("Example 2 Output:", Solution().maximumLength(nums2, k2))  # Expected: 4
