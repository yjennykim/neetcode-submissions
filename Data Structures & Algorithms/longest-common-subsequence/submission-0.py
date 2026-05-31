class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        grid = []
        for i in range(m+1):
            grid.append([0] * (n+1))
        print(grid)

        for c in range(n-1, -1, -1):
            for r in range(m-1, -1, -1):
                if text2[c] == text1[r]:
                    grid[r][c] = grid[r+1][c+1] + 1
                else:
                    grid[r][c] = max(grid[r+1][c], grid[r][c+1])
        
        print(grid)
        return grid[0][0]