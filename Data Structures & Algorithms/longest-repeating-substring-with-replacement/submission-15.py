from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # start with a small window and expand 
        # replace the length of string - most frequent character. keep a count
        max_length = 0
        L = 0
        counter = defaultdict(int)

        def get_most_freq() -> int:
            return max(counter.values()) if counter else 0

        for R in range(len(s)):
            counter[s[R]] += 1
            
            while R-L+1 - get_most_freq() > k:
                counter[s[L]] -= 1
                L += 1

            max_length = max(max_length, R-L+1)
            
        
        return max_length


        
