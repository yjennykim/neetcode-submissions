class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                sq = j * j

                dp[i] = min(dp[i], dp[i - sq] + 1)
                j += 1
        
        print(dp)
        return dp[n]