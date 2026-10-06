class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_set = defaultdict(int)
        s_set = defaultdict(int)
        smallest = float('inf')
        smallest_substr = ""

        for c in t:
            t_set[c] += 1

        L = 0
        formed = 0
        required = len(t)
        for R in range(len(s)):
            s_set[s[R]] += 1
            
            # see if adding s[R] is a good move
            if s[R] in t_set and s_set[s[R]] <= t_set[s[R]]:
                formed += 1
            
            # if all letters are matching
            while formed == required:
                # --- MINIMAL FIX: Only update if strictly smaller ---
                if (R - L + 1) < smallest:
                    smallest = R - L + 1
                    smallest_substr = s[L:R+1]

                # shrink window
                s_set[s[L]] -= 1
                if s_set[s[L]] < t_set[s[L]]:
                    formed -= 1
                L += 1
            
        return smallest_substr