from collections import Counter

class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        total_counts = Counter(basket1) + Counter(basket2)
        
        for count in total_counts.values():
            if count % 2 != 0:
                return -1
        
        fruits_to_swap = []
        count1 = Counter(basket1)
        for fruit, total_count in total_counts.items():
            target = total_count // 2
            diff = count1.get(fruit, 0) - target
            
            for _ in range(abs(diff)):
                fruits_to_swap.append(fruit)

        fruits_to_swap.sort()
        
        min_val = min(total_counts.keys())
        total_cost = 0
        swaps_to_make = len(fruits_to_swap) // 2
        for i in range(swaps_to_make):
            total_cost += min(fruits_to_swap[i], 2 * min_val)
            
        return total_cost


# Example 1
basket1 = [4, 2, 2, 2]
basket2 = [1, 4, 1, 2]
solution = Solution()
print("Example 1 Output:", solution.minCost(basket1, basket2))  # Output: 1

# Example 2
basket1 = [2, 3, 4, 1]
basket2 = [3, 2, 5, 1]
print("Example 2 Output:", solution.minCost(basket1, basket2))  # Output: -1
