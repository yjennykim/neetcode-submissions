class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        ways = [0] * len(s)
        if '1' <= s[0] <= '9':
            ways[0] = 1
        if len(s) == 1:
            return ways[0]

        if '1' <= s[1] <= '9' and '10' <= s[:2] <= '26':
            ways[1] = 2
        elif '10' <= s[:2] <= '26':
            ways[1] = 1
        elif '1' <= s[1] <= '9':
            ways[1] = 1

        for i in range(2, len(s)):
            count = 0
            if '1' <= s[i] <= '9' and '10' <= s[i-1: i+1] <= '26':
                ways[i] = ways[i-2] + ways[i-1]
            elif '10' <= s[i-1: i+1] <= '26':
                ways[i] = ways[i-2]
            elif '1' <= s[i] <= '9':
                ways[i] = ways[i-1]
        
        return ways[len(s)-1]