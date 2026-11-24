class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 0 = avail
        # 1 = obstacle
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [([0] * c) for _ in range(r)]
        dp[0][0] = 1

        for i in range(r):
            for j in range(c):
                if i > 0 and obstacleGrid[i-1][j] == 0:
                    dp[i][j] += dp[i-1][j]
                
                if j > 0 and obstacleGrid[i][j-1] == 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[r-1][c-1] if obstacleGrid[r-1][c-1] != 1 else 0
                    