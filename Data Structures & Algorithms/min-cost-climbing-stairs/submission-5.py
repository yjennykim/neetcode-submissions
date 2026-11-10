class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # base case
        if n == 0: return 0
        if n == 1: return cost[0]

        best = [0] * (n+1)


        for i in range(2, n+1):
            best[i] = min(best[i-1] + cost[i-1], best[i-2] + cost[i-2])
        
        return best[n]