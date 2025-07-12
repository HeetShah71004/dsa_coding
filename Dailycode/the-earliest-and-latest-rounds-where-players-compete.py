from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        earliest = float('inf')
        latest = -1

        def backtrack(players, round_num):
            nonlocal earliest, latest
            n = len(players)
            if n < 2:
                return
            next_round = [0] * (n // 2 + n % 2)

            for mask in range(1 << (n // 2)):
                bit = 1
                should_continue = False
                for i in range(n // 2):
                    if players[i] == firstPlayer and players[n - i - 1] == secondPlayer:
                        if round_num < earliest:
                            earliest = round_num
                        if round_num > latest:
                            latest = round_num
                        return
                    if (players[i] == firstPlayer or players[i] == secondPlayer) and (mask & bit) == 0:
                        should_continue = True
                        break
                    if (players[n - 1 - i] == firstPlayer or players[n - 1 - i] == secondPlayer) and (mask & bit) != 0:
                        should_continue = True
                        break
                    next_round[i] = players[i] if (mask & bit) != 0 else players[n - 1 - i]
                    bit = bit << 1
                if should_continue:
                    continue
                if n % 2 == 1:
                    next_round[n // 2] = players[n // 2]
                next_round.sort()
                backtrack(next_round, round_num + 1)

        backtrack(list(range(1, n + 1)), 1)
        return [earliest, latest]

# -------------------------------
# Example 1
sol = Solution()
n1, first1, second1 = 11, 2, 4
print(f"Example 1 Output: {sol.earliestAndLatest(n1, first1, second1)}")  # Output: [3, 4]

# Example 2
sol = Solution()
n2, first2, second2 = 5, 1, 5
print(f"Example 2 Output: {sol.earliestAndLatest(n2, first2, second2)}")  # Output: [1, 1]
