class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # def dfs(i, canBuy):
        #     if i >= len(prices):
        #         return 0

        #     if canBuy: 
        #         buy = dfs(i + 1, False) - prices[i]
        #         cooldown = dfs(i + 1, True)
        #         return max(cooldown, buy)
        #     else:
        #         sell = dfs(i + 2, True) + prices[i]
        #         cooldown = dfs(i + 1, False)
        #         return max(cooldown, sell)
            
        # return dfs(0, True)

        def profit():
            dp = [[0] * 2 for _ in range(len(prices) + 2)]

            for i in range(len(prices) - 1, -1, -1):
                # can buy
                buy = dp[i+1][False] - prices[i]
                cooldown = dp[i+1][True]
                dp[i][True] = max(cooldown, buy)

                # can't buy
                sell = dp[i+2][True] + prices[i]
                cooldown = dp[i+1][False]
                dp[i][False] = max(cooldown, sell)

            return dp[0][True] 
        return profit()




