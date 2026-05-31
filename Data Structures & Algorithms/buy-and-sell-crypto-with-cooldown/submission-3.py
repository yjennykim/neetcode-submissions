class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # def dfs(i, canBuy):
        #     if i >= len(prices): 
        #         return 0
            
        #     if canBuy:
        #         buy = dfs(i+1, False) - prices[i]
        #         cool = dfs(i+1, True)
        #         return max(buy, cool)
        #     else:
        #         sell = dfs(i+2, True) + prices[i]
        #         cool = dfs(i+1, False)
        #         return max(sell, cool)
            
        # return dfs(0, True)

        dp = [[0] * 2 for _ in range(len(prices) + 2)]
        
        for i in range(len(prices)-1, -1, -1):
            # can buy = buy, or cool
            dp[i][True] = max(dp[i+1][False] - prices[i], dp[i+1][True])

            # can sell = sell, or cool
            dp[i][False] = max(dp[i+2][True] + prices[i], dp[i+1][False])
        
        return dp[0][True]
