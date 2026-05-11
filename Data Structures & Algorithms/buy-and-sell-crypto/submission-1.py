class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = -1
        for i, price in enumerate(prices):
            s = max(prices[i:])
            if m < s - price:
                m = s - price
        return 0 if m <= 0 else m