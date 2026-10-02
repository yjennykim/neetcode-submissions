class Solution:
    

    def checkInclusion(self, s1: str, s2: str) -> bool:
       # We know that size of s1 is the window
       # Counts must be the same in that window

       # Base case
        n = len(s1)
        if len(s2) < n:    
            return False
        
        s1_count = defaultdict(int)
        for key in s1:
            s1_count[key] += 1
        
        s2_count = defaultdict(int)
        L = 0
        for R in range(len(s2)):
            s2_count[s2[R]] += 1

            # Trim to maintain window size
            window_size = R - L + 1
            if window_size > n:
                s2_count[s2[L]] -= 1
                if s2_count[s2[L]] == 0:
                    del s2_count[s2[L]]
                
                L += 1


            if s2_count == s1_count:
                return True
        
        return False
            
            
