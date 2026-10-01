class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy low, sell high
        max_profit = 0

        L = 0
        for R in range(len(prices)):
            # Buy
            if prices[R] < prices[L]: 
                L = R
            
            # Sell
            max_profit = max(max_profit, prices[R] - prices[L])
            
        return max_profit
        