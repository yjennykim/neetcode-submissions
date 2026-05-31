class Solution:
    def countSubstrings(self, s: str) -> int:
        # base case
        if len(s) <= 1: return len(s)

        n = len(s)
        grid = [[False] * n for _ in range(n)]
        count = 0

        for j in range(n):
            for i in range(n):
                if j < i: continue
                if j == i:
                    grid[i][j] = True
                elif s[i] == s[j] and j-i+1 == 2:
                    grid[i][j] = True
                elif s[i] == s[j] and grid[i+1][j-1]:
                    grid[i][j] = True
                if grid[i][j]: count += 1
                
        return count