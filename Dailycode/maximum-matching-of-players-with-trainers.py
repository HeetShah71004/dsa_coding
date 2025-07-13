from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = j = count = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
                count += 1
            j += 1
        return count

# Example 1
players1 = [4, 7, 9]
trainers1 = [8, 2, 5, 8]
solution = Solution()
result1 = solution.matchPlayersAndTrainers(players1, trainers1)
print(f"Example 1 Output: {result1}")  # Expected: 2

# Example 2
players2 = [1, 1, 1]
trainers2 = [10]
result2 = solution.matchPlayersAndTrainers(players2, trainers2)
print(f"Example 2 Output: {result2}")  # Expected: 1
