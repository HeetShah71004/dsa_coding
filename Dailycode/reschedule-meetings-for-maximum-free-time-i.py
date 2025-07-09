from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n, busy = len(startTime), 0
        for i in range(k):
            busy += endTime[i] - startTime[i]

        if n == k:
            return eventTime - busy

        ans = startTime[k] - busy

        l = 0
        for r in range(k, n):
            busy += (endTime[r] - startTime[r]) - (endTime[l] - startTime[l])
            end = eventTime if r == n - 1 else startTime[r + 1]
            start = endTime[l]
            ans = max(ans, end - start - busy)
            l += 1
        return ans


# Test examples
def main():
    sol = Solution()

    # Example 1
    eventTime = 5
    k = 1
    startTime = [1, 3]
    endTime = [2, 5]
    print("Example 1 Output:", sol.maxFreeTime(eventTime, k, startTime, endTime))  # Expected: 2

    # Example 2
    eventTime = 10
    k = 1
    startTime = [0, 2, 9]
    endTime = [1, 4, 10]
    print("Example 2 Output:", sol.maxFreeTime(eventTime, k, startTime, endTime))  # Expected: 6

    # Example 3
    eventTime = 5
    k = 2
    startTime = [0, 1, 2, 3, 4]
    endTime = [1, 2, 3, 4, 5]
    print("Example 3 Output:", sol.maxFreeTime(eventTime, k, startTime, endTime))  # Expected: 0

if __name__ == "__main__":
    main()
