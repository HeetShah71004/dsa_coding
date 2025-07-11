from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ans = [0] * n
        times = [0] * n
        meetings.sort()

        for start, end in meetings:
            flag = False
            minind = -1
            val = float('inf')
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break
            if not flag:
                ans[minind] += 1
                times[minind] += (end - start)

        maxi = -1
        id = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i
        return id


# ---------- Test Cases ----------

sol = Solution()

# Example 1
n1 = 2
meetings1 = [[0, 10], [1, 5], [2, 7], [3, 4]]
print("Example 1 Output:", sol.mostBooked(n1, meetings1))  # Expected: 0

# Example 2
n2 = 3
meetings2 = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
print("Example 2 Output:", sol.mostBooked(n2, meetings2))  # Expected: 1
