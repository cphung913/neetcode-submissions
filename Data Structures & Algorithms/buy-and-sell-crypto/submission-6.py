class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - lowest)
            lowest = min(lowest, price)
        return max_profit