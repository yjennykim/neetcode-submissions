class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 0: return cost[0]
        if n == 1: return cost[1]

        min_cost = [0] * n
        for i in range(n):
            min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i]
        
        return min(min_cost[n-1], min_cost[n-2])
