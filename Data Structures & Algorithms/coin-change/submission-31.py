class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        DP = [math.inf] * (amount + 1)
        DP[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    DP[i] = min(DP[i - coin] + 1, DP[i])

        return DP[amount] if DP[amount] != math.inf else -1
                