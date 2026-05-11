class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = -1
        for i, price in enumerate(prices):
            s = sorted(prices[i:])[-1]
            if max < s - price:
                max = s - price
        return 0 if max <= 0 else max