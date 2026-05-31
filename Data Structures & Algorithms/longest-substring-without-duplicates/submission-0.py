class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        maxLength = 0
        curr = 0

        l = 0
        for r in s:
            while r in seen:
                seen.remove(s[l])
                l += 1
                curr -= 1

            seen.add(r)
            curr += 1
            maxLength = max(maxLength, curr)
        
        return maxLength

        """
            r = z
            l = 1
            seen = "xy
            curr = 2
            s = "zxyzxyz"

        """

