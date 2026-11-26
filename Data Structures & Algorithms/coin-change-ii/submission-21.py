class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # 1 way to make amount 0: pick no coins
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(amount + 1):
                total_ways = 0
                k = 0
                while coin > 0 and k * coin <= j:
                    total_ways += dp[i - 1][j - k * coin]
                    k += 1
                dp[i][j] = total_ways

        return dp[n][amount]