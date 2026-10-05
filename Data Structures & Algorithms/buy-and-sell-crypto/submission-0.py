from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0       # Buy day
        right = 1      # Sell day
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # prices[right] is cheaper than prices[left], so make right the new buy day
                left = right
            right += 1

        return max_profit