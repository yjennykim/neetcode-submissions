class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # make grid
        n,m = len(word1), len(word2)

        grid = [[math.inf] * (m + 1) for _ in range(n + 1)] # reversed

        # base case
        for j in range(m, -1, -1):
            grid[n][j] = m - j
        
        for i in range(n, -1, -1):
            grid[i][m] = n - i
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    grid[i][j] = grid[i+1][j+1]
                else:
                    grid[i][j] = min(grid[i+1][j+1], grid[i][j+1], grid[i+1][j]) + 1
                
        return grid[0][0]
        
        
