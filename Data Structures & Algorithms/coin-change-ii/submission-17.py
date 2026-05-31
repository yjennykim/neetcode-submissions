class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # 1 way to make 0

        for coin in coins:
            for j in range(amount + 1):
                """
                since we want to allow duplicates, for each i in 0:amount, update i + coin

                """
                if j + coin <= amount:
                    dp[j + coin] += dp[j]
        
        print(dp)
        return dp[amount]
