from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.mem = {}

        def dfs(start, total):
            if total > amount:
                return 0  # No valid combination
            
            if total == amount:
                return 1  # Found a valid combination
            
            if (start, total) in self.mem:
                return self.mem[(start, total)]  # Use cached result
            
            ways = 0
            for i in range(start, len(coins)):
                ways += dfs(i, total + coins[i])  # Continue from the same index
            
            self.mem[(start, total)] = ways  # Store computed result
            return ways

        return dfs(0, 0)
