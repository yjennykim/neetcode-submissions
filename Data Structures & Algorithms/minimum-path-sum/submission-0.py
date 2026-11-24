class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if i > 0 and j <= 0:
                    grid[i][j] += grid[i-1][j]
                elif i <= 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif i == 0 and j == 0:
                    continue
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                
        return grid[r-1][c-1]