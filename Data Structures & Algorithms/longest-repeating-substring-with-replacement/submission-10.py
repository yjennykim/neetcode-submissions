from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        l,r = 0,0
        longest = 0
        
        def calculate_frequent_char():
            return max(counter.values())

        while r < len(s):
            counter[s[r]] += 1

            highest_freq = calculate_frequent_char()
            while r-l+1 - highest_freq > k:
                counter[s[l]] -= 1
                l += 1
                frequent_key = calculate_frequent_char()
            
            longest = max(longest, r-l+1)
            r += 1

        return longest