from typing import List
from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Create an array of just end times for binary search
        end_times = [e[1] for e in events]

        # DP table: dp[i][j] = max value using first i events and attending at most j events
        dp = [[0] * (k+1) for _ in range(n+1)]

        for i in range(1, n+1):
            start, end, value = events[i-1]
            # Find last non-overlapping event
            idx = bisect_right(end_times, start-1)

            for j in range(1, k+1):
                # Skip event
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                # Take event
                dp[i][j] = max(dp[i][j], dp[idx][j-1] + value)

        return dp[n][k]


# Test examples
def main():
    sol = Solution()

    # Example 1
    events1 = [[1,2,4],[3,4,3],[2,3,1]]
    k1 = 2
    print("Example 1 Output:", sol.maxValue(events1, k1))  # Expected: 7

    # Example 2
    events2 = [[1,2,4],[3,4,3],[2,3,10]]
    k2 = 2
    print("Example 2 Output:", sol.maxValue(events2, k2))  # Expected: 10

    # Example 3
    events3 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    k3 = 3
    print("Example 3 Output:", sol.maxValue(events3, k3))  # Expected: 9

if __name__ == "__main__":
    main()
