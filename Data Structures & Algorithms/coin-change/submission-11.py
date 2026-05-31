from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # Handle edge cases where coins list is empty
        if not coins:
            return -1

        minCoins = [math.inf] * (amount + 1)  # Use amount+1 to include index 'amount'
        minCoins[0] = 0  # Base case: 0 coins to make amount 0

        for coin in coins:
            for i in range(coin, amount + 1):  # Start from 'coin' to avoid negative indexing
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

        return minCoins[amount] if minCoins[amount] != math.inf else -1
