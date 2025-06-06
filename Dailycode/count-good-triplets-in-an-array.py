class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n # position mapping: pos2[x] is the index of x in nums2
        for i, x in enumerate(nums2):
            pos2[x] = i

        M = [pos2[x] for x in nums1] # M[i] = pos2[nums1[i]]

        # Number of indices i < j s.t. M[i] < M[j]
        left, bit_left = [0] * n, BIT(n)
        for j in range(n):
            left[j] = bit_left.query(M[j])
            bit_left.update(M[j] + 1, 1)

        # Number of indices k > j s.t. M[k] > M[j]
        right, bit_right = [0] * n, BIT(n)
        for j in range(n - 1, -1, -1):
            right[j] = bit_right.query(n) - bit_right.query(M[j] + 1)
            bit_right.update(M[j] + 1, 1)
        
        # Count good triplets
        good_triplets = 0
        for j in range(n):
            good_triplets += left[j] * right[j]

        return good_triplets

# Test cases

nums1 = [2,0,1,3]
nums2 = [0,1,2,3]
solution = Solution()
result = solution.goodTriplets(nums1, nums2)
print(result)  # Output: 1