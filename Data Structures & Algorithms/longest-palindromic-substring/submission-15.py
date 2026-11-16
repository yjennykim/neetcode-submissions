class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        grid = [[False] * n for _ in range(n)]

        longest_len = 0
        longest_start = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 1 or grid[i + 1][j - 1]):
                    grid[i][j] = True

                    if j-i+1 > longest_len:
                        longest_len = j-i+1
                        longest_start = i
        
        
        return s[longest_start: longest_start + longest_len]