class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.best = math.inf

        if amount == 0:
            return 0

        self.memo = {}
        def dfs(total):
            if total > amount:
                return math.inf
            
            if total == amount:
                return 0

            if total in self.memo:
                return self.memo[total]

            min_coins = math.inf
            for i in range(len(coins)):
                count_take = dfs(total + coins[i]) + 1
                min_coins = min(count_take, min_coins)

            self.memo[total] = min_coins
            return min_coins

        min_coins = dfs(0)
        if min_coins == math.inf:
            return -1
        return min_coins
        
        