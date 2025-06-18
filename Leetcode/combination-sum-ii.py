class Solution:
    def combinationSum2(self, cand, target):
        cand.sort()
        res = []
        path = []
        self.dfs(cand, 0, target, path, res)
        return res

    def dfs(self, cand, cur, target, path, res):
        if target == 0:
            res.append(path.copy())
            return
        if target < 0:
            return

        for i in range(cur, len(cand)):
            if i > cur and cand[i] == cand[i - 1]:  # Skip duplicates
                continue
            path.append(cand[i])
            self.dfs(cand, i + 1, target - cand[i], path, res)
            path.pop()  # Backtrack


# Test Case 1
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
sol = Solution()
output1 = sol.combinationSum2(candidates1, target1)
print("Output for Test Case 1:")
print(output1)
# Expected: [[1,1,6],[1,2,5],[1,7],[2,6]]

# Test Case 2
candidates2 = [2, 5, 2, 1, 2]
target2 = 5
sol = Solution()
output2 = sol.combinationSum2(candidates2, target2)
print("\nOutput for Test Case 2:")
print(output2)
# Expected: [[1,2,2],[5]]
