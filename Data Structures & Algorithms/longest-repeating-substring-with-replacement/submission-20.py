class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1

            replacements = (r-l+1) - max(counts.values())
            while replacements > k and l <= r:
                counts[s[l]] -= 1
                l += 1
                replacements = (r-l+1) - max(counts.values())

            longest = max(longest, r-l+1)

        return longest


