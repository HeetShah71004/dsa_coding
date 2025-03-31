class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0
        
        pair_sums = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i + 1])
        
        pair_sums.sort()
        
        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])
        
        return max_score - min_score

# Test cases

weights = [1,3,5,1]
k = 2

solution = Solution()

print(solution.putMarbles(weights, k)) # Output: 4