class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # size (n+1) 
        dp = [False] * (n + 1)
        dp[n] = True
        word_set = set(wordDict)
        sizes = set()
        for word in word_set:
            sizes.add(len(word))
        for i in range(n-1,-1,-1):
            for size in sizes:
                # slicing s[i+size] and dp[i+size]
                # if s[n-1-size: i] in word_set or i + size == n:
                    # dp[i] = dp[i + size]
                if i + size <= n:
                    if s[i:i+size] in word_set and dp[i+size]:
                        dp[i] = True
                        break
        
        return dp[0]
