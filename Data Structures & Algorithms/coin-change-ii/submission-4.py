from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.numCombos = 0
        self.mem = {}

        def dfs(start, total):
            if total > amount:
                return
            
            if total == amount:
                self.numCombos += 1
                return
            
            if (start, total) in self.mem:
                self.numCombos += self.mem[(start, total)]
                return
            
            prevNumCombos = self.numCombos  # Store current count before recursion
            
            for i in range(start, len(coins)):
                dfs(i, total + coins[i])
            
            # Store the newly added combinations
            self.mem[(start, total)] = self.numCombos - prevNumCombos

        dfs(0, 0)
        return self.numCombos
