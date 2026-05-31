class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low
        # sell high
        maxProfit = 0

        if len(prices) < 1: 
            return 0

        curr = prices[0]
        for stock in prices:
            if stock < curr:
                curr = stock
            maxProfit = max(maxProfit, stock - curr)
        
        return maxProfit
