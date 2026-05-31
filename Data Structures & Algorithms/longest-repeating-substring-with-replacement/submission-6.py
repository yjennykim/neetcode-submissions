class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxLength = 0
        maxCount = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            
            # Update the maxCount for the current character
            maxCount = max(maxCount, count[s[r]])
            
            # Check if we need to shrink the window
            while (r - l + 1) - maxCount > k:
                count[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)

        return maxLength
