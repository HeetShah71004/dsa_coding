from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]] + [startTime[i] - endTime[i-1] for i in range(1, n)] + [eventTime - endTime[-1]]
        dur = [endTime[i] - startTime[i] for i in range(n)]
        initial_max = max(gaps)

        v1 = v2 = v3 = -1
        c1 = c2 = c3 = 0

        for g in gaps:
            if g > v1:
                v3, c3 = v2, c2
                v2, c2 = v1, c1
                v1, c1 = g, 1
            elif g == v1:
                c1 += 1
            elif g > v2:
                v3, c3 = v2, c2
                v2, c2 = g, 1
            elif g == v2:
                c2 += 1
            elif g > v3:
                v3, c3 = g, 1
            elif g == v3:
                c3 += 1

        res = initial_max
        for k in range(n):
            a, b = gaps[k], gaps[k+1]
            cnt1 = (a == v1) + (b == v1)
            if cnt1 < c1:
                max_other = v1
            else:
                cnt2 = (a == v2) + (b == v2)
                if cnt2 < c2:
                    max_other = v2
                else:
                    max_other = v3

            m = a + dur[k] + b
            if max_other >= dur[k]:
                ans_k = m if m > max_other else max_other
            else:
                ans_k = m - dur[k]
            if ans_k > res:
                res = ans_k
        return res


# Testing examples
sol = Solution()

# Example 1
print("Example 1 Output:", sol.maxFreeTime(eventTime=5, startTime=[1,3], endTime=[2,5]))  # Output: 2

# Example 2
print("Example 2 Output:", sol.maxFreeTime(eventTime=10, startTime=[0,7,9], endTime=[1,8,10]))  # Output: 7

# Example 3
print("Example 3 Output:", sol.maxFreeTime(eventTime=10, startTime=[0,3,7,9], endTime=[1,4,8,10]))  # Output: 6

# Example 4
print("Example 4 Output:", sol.maxFreeTime(eventTime=5, startTime=[0,1,2,3,4], endTime=[1,2,3,4,5]))  # Output: 0
