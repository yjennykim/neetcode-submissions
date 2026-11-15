class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        grid = [[False] * n for _ in range(n)]

        longest_len = 0
        longest_start = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # j - i <= 1 is so we don't look at left side of triangle. We need to set all diagnal to True
                if s[i] == s[j] and (j-i <= 1 or grid[i+1][j-1]):
                    # Case 1: Length 1 (j - i == 0, e.g., "a")
                    # Case 2: Length 2 (j - i == 1, e.g., "aa")
                    # Case 3: Length 3 or more (j - i >= 2, e.g., "aba", "abba")
                    grid[i][j] = True
                    if j-i+1 > longest_len:
                        longest_len = j-i+1
                        longest_start = i
        return s[longest_start: longest_start + longest_len]