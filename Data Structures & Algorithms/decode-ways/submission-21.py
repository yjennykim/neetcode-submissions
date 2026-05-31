class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0": return 0
        if len(s) == 1: return 1

        ways = [0] * len(s)

        # base cases
        ways[0] = 1 

        if 10 <= int(s[:2]) <= 26:
            ways[1] = 1

        if int(int(s[1]) != 0):
            ways[1] += 1

        for i in range(2, len(s)):
            # two digit case
            if 10 <= int(s[i-1:i+1]) <= 26:
                ways[i] = ways[i-2]
            
            # one digit case
            if int(s[i]) != 0:
                ways[i] += ways[i-1]

        print("ways", ways)
        return ways[len(s)-1]