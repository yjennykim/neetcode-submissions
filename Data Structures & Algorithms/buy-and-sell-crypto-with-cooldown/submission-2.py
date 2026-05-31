class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, canBuy):
            if i >= len(prices): 
                return 0
            
            if canBuy:
                buy = dfs(i+1, False) - prices[i]
                cool = dfs(i+1, True)
                return max(buy, cool)
            else:
                sell = dfs(i+2, True) + prices[i]
                cool = dfs(i+1, False)
                return max(sell, cool)
            
        return dfs(0, True)