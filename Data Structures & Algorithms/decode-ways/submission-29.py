class Solution:
    def numDecodings(self, s: str) -> int:
        ct = 0
        n = len(s)
        if not s or s[0] == "0":
            return 0
            
        ways = [0] * n
        
        if n <= 1:
            return n

        ways[0] = 1 
        for i in range(1, n):
            # number of ways to decode 
            if s[i] != "0":
                ways[i] += ways[i-1]

            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                if i == 1:
                    ways[i] += 1
                else:
                    ways[i] += ways[i-2]
             
        return ways[n-1]