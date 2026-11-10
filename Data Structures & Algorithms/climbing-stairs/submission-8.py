class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        # n = 1, n = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        
        return ways[n]