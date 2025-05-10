# 121. best-time-to-buy-and-sell-stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        best_buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > best_buy:
                max_profit = max(max_profit, prices[i] - best_buy)
            best_buy = min(best_buy, prices[i])
        
        return max_profit

# Test Case 1: Basic profit scenario
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # Expected output: 5

# Test Case 2: No profit possible (prices keep decreasing)
print(Solution().maxProfit([7, 6, 4, 3, 1]))     # Expected output: 0
