class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxLength = 0
        length = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            
            mostFrequent = max(count.values())
            while (r-l+1) - mostFrequent > k:
                count[s[l]] -= 1
                l += 1
                mostFrequent = max(count.values())
                length -= 1
                print("Window:", s[l:r+1])

            maxLength = max(maxLength, r-l+1)

        return maxLength


