class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # if every coin is bigger than amount 
        if amount < min(coins):
            return -1

        minCoins = [math.inf] * (amount)

        # base case
        for coin in coins:
            if coin <= amount:
                minCoins[coin-1] = 1

        for i in range(min(coins), amount):
            for coin in coins:
                if i-coin >= 0 and minCoins[i] != 1:
                    minCoins[i] = min(minCoins[i-coin] + 1, minCoins[i])
        
        print(minCoins)
        return minCoins[-1] if minCoins[-1] != math.inf else -1



        
        