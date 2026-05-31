class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        OPT = [0] * (len(cost) + 1)
        OPT[0] = cost[0]
        OPT[1] = cost[1]
        
        for i in range(2, len(cost)):
            OPT[i] = min(OPT[i-1], OPT[i-2]) + cost[i]

        OPT[len(cost)] = min(OPT[len(cost)-1], OPT[len(cost)-2])
        print(OPT)
        return OPT[len(cost)]