from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] will store the number of ways to make amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # There's one way to make amount 0, by using no coins
        
        # Process each coin
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]  # Add ways to make (i - coin) to dp[i]
        
        return dp[amount]  # The number of ways to make the target amount
