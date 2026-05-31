class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        self.mem = {}

        def dfs(total):
            if total > amount:
                return math.inf
            
            if total == amount:
                return 0

            if total in self.mem:
                return self.mem[total]
            minCoins = math.inf
            for coin in coins:
                count = dfs(total + coin) + 1
                minCoins = min(minCoins, count)
            
            self.mem[total] = minCoins
            return minCoins
        
        minCoins = dfs(0)
        if minCoins == math.inf:
            return -1
        
        return minCoins