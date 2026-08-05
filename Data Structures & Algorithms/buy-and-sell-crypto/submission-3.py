class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0

        for i in range(len(prices)):
            profit = max(prices[i:]) - prices[i]
            if profit > highest:
                highest = profit
        return highest
