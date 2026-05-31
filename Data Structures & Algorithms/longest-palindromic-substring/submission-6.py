class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case
        if len(s) <= 1: return s

        n = len(s)
        grid = [[False] * n for _ in range(n)]

        maxLength = 0
        longestI, longestJ = 0, 1

        for j in range(n):
            for i in range(n):
                if j < i: continue
                if j == i:
                    grid[i][j] = True
                elif s[i] == s[j] and j-i+1 == 2:
                    grid[i][j] = True
                elif s[i] == s[j] and grid[i+1][j-1]:
                    grid[i][j] = True
                
                if grid[i][j] == True and j-i+1 > maxLength:
                    maxLength = j-i+1
                    longestI = i
                    longestJ = j
                    print(f'i={i} j={j}')
        return s[longestI: longestJ+1]